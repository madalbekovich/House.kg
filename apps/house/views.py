# framework packages
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# your import 
from apps.house import models
from apps.house import serializers
from apps.house.utils import add_watermark
from rest_framework.permissions import IsAuthenticated
from apps.house import filters

class ComplexView(viewsets.GenericViewSet):
    queryset = models.ResidentialCategory.objects.all()
    serializer_class = serializers.ResidentialCategorySerializer
    
    @action(detail=False, methods=['get'])
    def complex_list(self, request, *args, **kwargs):
        instance = models.ResidentialCategory.objects.filter(parent=None)
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CitiesView(viewsets.GenericViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.RegionsSerializer
    
    @action(detail=False, methods=['get'], url_path='regions')
    def regions(self, request, *args, **kwargs):
        city = request.query_params.get('city')
        region = models.Location.objects.filter(parent=None) if not city else \
            get_object_or_404(models.Location, id=city).get_children()
        serializer = serializers.CitiesSerializer(region, many=True, context={"empty_㋡": True})  
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PropertyView(viewsets.GenericViewSet):
    queryset = models.Property.objects.select_related(
        'location' ,'documents', 'miscellaneous', 'contact_info', 'complex_name').all().order_by('-id')
    serializer_class = serializers.AddPropertySerializer
    filter_backends = [DjangoFilterBackend, ]
    # permission_classes = [IsAuthenticated, ]
    filterset_class = filters.PropertyFilter
    
     
    @action(detail=False, methods=['post'])
    def add(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def property(self, request, *args, **kwagrs):
        print({"GETting data query": request.query_params})
        instance = self.filter_queryset(self.get_queryset())
        serializer = serializers.PropertySerializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['delete'], url_path=None)
    def remove(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"pohui": True}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'], url_path=None)
    def edit(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)