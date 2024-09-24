from rest_framework import serializers
from apps.house import models
from apps.house.mixins import HierarchicalMixin


class ResidentialCategorySerializer(serializers.ModelSerializer, HierarchicalMixin):
    children = serializers.SerializerMethodField()
    class Meta:
        model = models.ResidentialCategory
        fields = ['id', 'complex_name', 'building_date', 'level', 'parent', 'children']
    
    def get_children(self, instance):
        return super().base_method(instance)
        

class MiscellaneousSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Miscellaneous
        fields = '__all__'

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Security
        fields = '__all__'
        
class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Documents
        fields = '__all__'
        
class ContactInfoSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=False)
    class Meta:
        model = models.ContactInfo
        fields = [
            'advertiser_type', 'phone_number',
        ]

class CitiesSerializer(serializers.ModelSerializer, HierarchicalMixin):
    children = serializers.SerializerMethodField()
    class Meta:
        model = models.Location
        fields = [
            'id',
            'city', 'lat',
            'lng', 'population',
            'iso2', 'capital', 'lft',
            "rght", "tree_id", "level", "parent",
            'children'
        ]
    
    def get_children(self, obj):
        return super().base_method(obj)

class RegionsSerializer(serializers.ModelSerializer, HierarchicalMixin):
    class Meta:
        model = models.Location
        fields = [
            'id',
            'city', 'lat',
            'lng', 'population',
            'iso2', 'capital', 'lft',
            "rght", "tree_id", "level", "parent",
        ]
        
class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pictures
        fields = ['pictures', ]
        
class AddPropertySerializer(serializers.ModelSerializer):
    security = SecuritySerializer(required=False)
    miscellaneous = MiscellaneousSerializer(required=False)
    documents = DocumentsSerializer()
    contact_info = ContactInfoSerializer(required=False)
    properties_pictures = PicturesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )
    class Meta:
        model = models.Property
        fields = [
            'id',
            'type_deal',
            'type_property', 
            'room_count', 'type_series',
            'type_building', 'year_construction', 
            'floor_number', 'total_floors', 'general', 
            'residential', 'kitchen', 'type_heating', 'type_condition',
            'eni_code', 'street', 'house_number', 'intersection_with', 'lat',
            'lon', 'youtube_url', 'location', 'price', 'currency', 'price_for', 'installment_type',
            'mortage_type', 'exchange_type', 
            'complex_name',
            'security',
            "miscellaneous",
            'documents',
            'properties_pictures',
            'uploaded_images',
            'contact_info',
        ]

    def create(self, validated_data):
        request_user = self.context['request'].user
        phone_number = getattr(request_user, 'name', 'not found phone')
        
        contact_info_data = validated_data.pop('contact_info', {})
        contact_info_data['phone_number'] = phone_number  #
        
        documents_data = validated_data.pop('documents', None)
        security_data = validated_data.pop('security', None)
        miscellaneous_data = validated_data.pop('miscellaneous', None)  
        uploaded_images = validated_data.pop('uploaded_images', [])

        # Инициализация переменных как None
        document_instance = None
        security_instance = None
        miscellaneous_instance = None
        contact_instance = None

        # Создание объектов, если данные предоставлены
        if documents_data:
            document_instance = models.Documents.objects.create(**documents_data)
            
        if security_data:
            security_instance = models.Security.objects.create(**security_data)
            
        if miscellaneous_data:
            miscellaneous_instance = models.Miscellaneous.objects.create(**miscellaneous_data)
            
        if contact_info_data: 
            contact_instance = models.ContactInfo.objects.create(**contact_info_data)

        # Создание объекта Property
        property_instance = models.Property.objects.create(
            user=request_user,
            contact_info=contact_instance,  # может быть None, если contact_info отсутствует
            documents=document_instance,  # может быть None, если documents отсутствует
            security=security_instance,  # может быть None, если security отсутствует
            miscellaneous=miscellaneous_instance,  # может быть None, если miscellaneous отсутствует
            **validated_data
        )

        # Создание изображений
        for image in uploaded_images:
            models.Pictures.objects.create(property=property_instance, pictures=image)
            
        return property_instance
    
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = "__all__"