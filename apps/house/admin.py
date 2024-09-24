from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from apps.house import models

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Location

admin.site.register(Location, MPTTModelAdmin)

@admin.register(models.ResidentialCategory)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('complex_name', 'parent')
    search_fields = ('complex_name',)

class PicteresInline(admin.TabularInline):
    '''Tabular Inline View for Property '''
    model = models.Pictures
    extra = 1
    
@admin.register(models.Property)
class Property(admin.ModelAdmin):
    inlines = [PicteresInline,  ]