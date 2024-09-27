from rest_framework import serializers
from apps.house import models
from apps.house.mixins import HierarchicalMixin
from drf_writable_nested import WritableNestedModelSerializer


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
        
class AddPropertySerializer(WritableNestedModelSerializer):
    security = SecuritySerializer(required=False)
    miscellaneous = MiscellaneousSerializer(required=False)
    documents = DocumentsSerializer(required=False)
    properties_pictures = PicturesSerializer(many=True, required=False)
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
            'mortage_type', 'exchange_type', 'advertiser_type', 'phone_number',
            'complex_name',
            'security',                                                                                                                                                                                                                                                           
            "miscellaneous",
            'documents',
            'properties_pictures',
        ]
    
class PropertySerializer(serializers.ModelSerializer):
    location = RegionsSerializer()
    complex_name = ResidentialCategorySerializer()
    security = SecuritySerializer(read_only=True)
    miscellaneous = MiscellaneousSerializer(read_only=True)
    documents = DocumentsSerializer(read_only=True)
    properties_pictures = PicturesSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Property
        fields = "__all__"
        # exclude = ('complex_name', )