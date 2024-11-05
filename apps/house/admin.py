from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.house import models
from django_admin_geomap import ModelAdmin as MapAdmin
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from apps.house import data_models

class ComplexPicteresInline(admin.TabularInline):
    '''Tabular Inline View for Property '''
    model = models.ComplexImage
    extra = 1
    
@admin.register(models.ResidentialCategory)
class CategoryAdmin(MapAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "74.6066926"
    geomap_default_latitude = "42.8777895"
    geomap_default_zoom = "12"
    geomap_height = "500px"
    list_display = ('complex_name', 'object_state', 'get_media')
    search_fields = ('complex_name', 'id')
    inlines = [ComplexPicteresInline, ]

    def get_media(self, obj):
        if obj.media:
            return mark_safe(f"<img src='{obj.media.url}' height='61' width='80'>")
        return None
    get_media.short_description = 'видимость обьекта'

class PicteresInline(admin.TabularInline):
    '''Tabular Inline View for Property '''
    model = models.Pictures
    extra = 1
    
@admin.register(models.Property)
class Property(admin.ModelAdmin):
    list_display = ['id', 'active_post']
    search_fields = ['user__username']
    inlines = [PicteresInline,  ]
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.category:
            if obj.category.id == 1:
                form.base_fields.pop('material', None)
                form.base_fields.pop('rental_term', None)
                form.base_fields.pop('irrigation', None)
                form.base_fields.pop('land_options', None)
                form.base_fields.pop('land_amenities', None)
                form.base_fields.pop('land_location', None)
                form.base_fields.pop('water', None)
                form.base_fields.pop('canalization', None)
                form.base_fields.pop('electricity', None)
                form.base_fields.pop('options', None)
                form.base_fields.pop('room_location', None)
                form.base_fields.pop('flat_options', None)
                form.base_fields.pop('toilet', None)
                form.base_fields.pop('commercial_type', None)
                form.base_fields.pop('parking_type', None)
                
        return form