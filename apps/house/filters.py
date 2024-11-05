# packages
from django_filters import rest_framework as filters
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django.contrib.gis.db.models import PointField

# your import 
from apps.house import models

class PropertyFilter(filters.FilterSet, GeoFilterSet):
    # GeoFilterSet
    polygon = GeometryFilter(field_name='point', lookup_expr='within')
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    year_min = filters.NumberFilter(field_name='year_construction', lookup_expr='gte', label='Год постройки от')
    year_max = filters.NumberFilter(field_name='year_construction', lookup_expr='lte', label='Год постройки до')
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    
    class Meta:
        model = models.Property
        fields = '__all__'
        filter_overrides = {
            PointField: {
                'filter_class': GeometryFilter
            }
        }