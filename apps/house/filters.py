# packages
from django_filters import rest_framework as filters

# your import 
from apps.house import models
from apps.house import choices

class PropertyFilter(filters.FilterSet):
    type_deal = filters.ChoiceFilter(field_name='type_deal', choices=choices.TYPE_DEAL)
    type_property = filters.ChoiceFilter(field_name='type_property',  choices=choices.PROPERTY_TYPE_OPTIONS)
    
    class Meta:
        model = models.Property
        fields = ['type_deal', 'type_property',]