# tiffin_app/views.py
from django.shortcuts import render
from .models import MealPackage, TiffinServiceProvider
from django.db.models import Q # For complex queries

def list_meal_packages(request):
    query = request.GET.get('location_filter', '')
    packages = MealPackage.objects.filter(is_active=True).select_related('tiffin_service_provider')

    if query:
        packages = packages.filter(
            Q(service_area_city__icontains=query) |
            Q(tiffin_service_provider__operating_city_area__icontains=query)
        ).distinct()

    # Get unique locations for the filter dropdown
    package_locations = MealPackage.objects.filter(is_active=True)\
                                         .values_list('service_area_city', flat=True)\
                                         .distinct().order_by('service_area_city')
    provider_locations = TiffinServiceProvider.objects.values_list('operating_city_area', flat=True)\
                                                    .distinct().order_by('operating_city_area')

    # Combine and make unique, filtering out empty/None and sorting
    all_locations_set = set(list(package_locations) + list(provider_locations))
    sorted_locations = sorted([loc for loc in all_locations_set if loc and loc.strip()])

    context = {
        'meal_packages': packages,
        'available_locations': sorted_locations,
        'current_filter': query,
        'page_title': 'Available Tiffin Packages'
    }
    return render(request, 'tiffin_app/meal_package_list.html', context)