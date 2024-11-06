# framework packages
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.utils import translation
from apps.house import exceptions
from rest_framework import mixins as rest_mixin

# your import 
from apps.house import models
from apps.house import serializers
from apps.house import data_serializers
from apps.house import data_models
from apps.house import filters
from apps.helpers import pagination
from apps.house import mixins
from apps.house import choices
from apps.house.tasks import delete_post
# from apps.house import exceptions


class ComplexView(viewsets.GenericViewSet):
    queryset = models.ResidentialCategory.objects.all()
    serializer_class = serializers.ResidentialCategorySerializer
    
    @action(detail=False, methods=['get'])
    def buildings(self, request, *args, **kwargs):
        complex_id = request.query_params.get('complex_id')
        
        if complex_id:
            query_complex = get_object_or_404(models.ResidentialCategory, id=complex_id)
            serializer_complex = serializers.ResidentialCategorySerializer(query_complex).data
            return Response(serializer_complex, status=status.HTTP_200_OK)
    
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'])
    def add_buildings(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "complex succes created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PropertyView(rest_mixin.ListModelMixin, viewsets.GenericViewSet, mixins.ViewsMixin):
    queryset = models.Property.objects.prefetch_related('land_amenities', 'options', 'safety', 'land_options', 'room_options', 'flat_options').all().order_by('-id')
    serializer_class = serializers.AddPropertySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.PropertyFilter
    pagination_class = pagination.PropertyResultsPagination
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.get_serializer_class()
        return serializers.PropertySerializer
     
    @action(detail=False, methods=['post'], url_path=None)
    def set(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            property_instance = serializer.save(user=request.user)
            if 'properties_pictures' in request.data:
                pictures_data = request.data.getlist('properties_pictures') 
                for picture in pictures_data:
                    models.Pictures.objects.create(pictures=picture, property=property_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'], url_path=None)
    def post_control(self, request, *args, **kwargs):
        instance = self.get_object()
        activate = request.query_params.get('activate', 'false').lower() == 'true'
        if activate:
            instance.active_post = True
            instance.save()
            return Response({"message ": "Post activated!"}, status=status.HTTP_200_OK)
        instance.active_post = False
        instance.save()
        instance_id = str(instance.id)
        delete_post.delay(instance_id)
        return Response({"message": "Post archived!"}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'], url_path=None)
    def edit(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataView(APIView):
    serializer_class = data_serializers.CombinedSerializer
    def get(self, request):
        data = {
            'type': data_models.Type.objects.all(),
            'category': data_models.Category.objects.all(),
            'rooms': data_models.Rooms.objects.all(),
            'material': data_models.Material.objects.all(),
            'floors': data_models.Floor.objects.all(),
            'condition': data_models.Condition.objects.all(),
            'owner_type': data_models.AccountType.objects.all(),
            'heating': data_models.Heating.objects.all(),
            'region': data_models.Region.objects.all(),
            'irrigation': data_models.Irrigation.objects.all(),
            'land_options': data_models.LandOptions.objects.all(),
            'land_location': data_models.LandLocation.objects.all(),
            'rental_term': data_models.RentalTerm.objects.all(),
            'land_amenities': data_models.LandAmenities.objects.all(),
            'room_option': data_models.RoomOption.objects.all(),
            'water': data_models.Water.objects.all(),
            'electricity': data_models.Electricity.objects.all(),
            'options': data_models.Options.objects.all(),
            'finishing': data_models.Finishing.objects.all(),
            'canalization': data_models.Canalization.objects.all(),
            'comment_allowed': data_models.CommentAllowed.objects.all(),
            'parking_type': data_models.ParkingType.objects.values('id', 'translations__name'),
            'commercial_type': data_models.CommercialType.objects.values('id', 'translations__name'),
            'town': data_models.Town.objects.all(),
            'phone_info': data_models.Phone.objects.all(),
            'internet': data_models.Internet.objects.all(),
            'toilet': data_models.Toilet.objects.all(),
            'gas': data_models.Gas.objects.all(),
            'balcony': data_models.Balcony.objects.all(),
            'door': data_models.Door.objects.all(),
            'parking': data_models.Parking.objects.all(),
            'furniture': data_models.Furniture.objects.all(),
            'flooring': data_models.Flooring.objects.all(),
            'safety': data_models.Safety.objects.all(),
            'flat_options': data_models.FlatOptions.objects.all(),
            'exchange': data_models.Exchange.objects.all(),
            'price_type': data_models.PriceType.objects.all(),
            'currency': data_models.Currency.objects.all(),
            'possibility': data_models.Possibility.objects.all(),
            'document': data_models.Document.objects.all(),
            'district': data_models.District.objects.all(),
        }
        
        serializer = self.serializer_class(data)
        return Response(serializer.data)
    
class PropertyParam(APIView):
    def get(self, request):
        if request.query_params.get('show_fields') == 'true':
            return self.show_fields(request)

        validation_result = self.validate_params(request)
        
        if 'error' in validation_result:
            return Response(validation_result, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"success": "Все параметры валидны"}, status=status.HTTP_200_OK)

    def validate_params(self, request):
        type_deal = request.query_params.get('type_deal')
        type_property = request.query_params.get('type_property')
        region_id = request.query_params.get('region_id')  
        town_id = request.query_params.get('town_id')
        
        rules = exceptions.get_validation_rules(region_id, town_id).get(type_deal, {}).get(type_property)

        if not rules:
            return {"error": "Invalid type_deal or type_property"}

        missing_fields = []
        invalid_fields = []

        for rule in rules:
            field_name = rule['name']
            required = rule.get('required', False)
            value = request.query_params.get(field_name)

            if required and not value :
                missing_fields.append(field_name)

        available_fields = [
            {
                "name": rule['name'],
                "type": rule['type'],
                "required": rule['required'],
                "data": rule.get('data', []),
            }
            for rule in rules
        ]

        response = {}
        if missing_fields:
            response.update({
                "error": "Missing required fields",
                "missing_fields": missing_fields,
            })
        if invalid_fields:
            response.update({
                "error": "Invalid fields",
                "invalid_fields": invalid_fields,
            })

        response["available_fields"] = available_fields
        return response if response else {"success": "All fields are valid"}

    def show_fields(self, request):
        type_deal = request.query_params.get('type_deal')
        type_property = request.query_params.get('type_property')

        rules = exceptions.VALIDATION_RULES.get(type_deal, {}).get(type_property)
        
        if not rules:
            return Response({"error": "Invalid type_deal or type_property"}, status=status.HTTP_400_BAD_REQUEST)

        fields_info = []
        for rule in rules:
            field_info = {
                "name": rule['name'],
                "type": rule['type']
            }
            if 'choices' in rule:
                field_info['choices'] = rule['choices']
            fields_info.append(field_info)
        
        return Response({"fields": fields_info}, status=status.HTTP_200_OK)