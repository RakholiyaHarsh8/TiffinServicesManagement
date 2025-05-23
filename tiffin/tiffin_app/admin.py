# tiffin_app/admin.py
from django.contrib import admin
from .models import TiffinServiceProvider, MealPackage

actions = ['mark_active', 'mark_inactive']
name_label = "Tiffin Service Provider"
def mark_active(self, request, queryset):
    queryset.update(is_active=True)
mark_active.short_description = "Mark selected packages as active"

def mark_inactive(self, request, queryset):
    queryset.update(is_active=False)
mark_inactive.short_description = "Mark selected packages as inactive"

@admin.register(TiffinServiceProvider)
class TiffinServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'contact_number', 'email', 'operating_city_area', 'meal_type_offered')
    search_fields = ('name', 'owner_name', 'operating_city_area', 'email')
    list_filter = ('meal_type_offered', 'operating_city_area')
    fieldsets = (
        (None, {
            'fields': ('name', 'owner_name', 'contact_number', 'email')
        }),
        ('Service Details', {
            'fields': ('operating_city_area', 'meal_type_offered', 'delivery_options')
        }),
    )

@admin.register(MealPackage)
class MealPackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'tiffin_service_provider', 'meal_type', 'price', 'duration', 'service_area_city', 'is_active')
    list_filter = ('meal_type', 'duration', 'service_area_city', 'is_active', 'tiffin_service_provider')
    search_fields = ('package_name', 'description', 'tiffin_service_provider__name', 'service_area_city')
    list_editable = ('price', 'is_active')
    autocomplete_fields = ['tiffin_service_provider']

    fieldsets = (
        (None, {
            'fields': ('tiffin_service_provider', 'package_name', 'description', 'image')
        }),
        ('Package Details', {
            'fields': ('meal_type', 'price', 'duration', 'service_area_city')
        }),
        ('Status', {
            'fields': ('is_active',)
        })
    )