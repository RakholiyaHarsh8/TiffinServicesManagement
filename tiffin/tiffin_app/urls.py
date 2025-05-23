# tiffin_app/urls.py
from django.urls import path
from . import views  # This line imports views from your tiffin_app/views.py

app_name = 'tiffin_app' # Optional, but good practice for namespacing

urlpatterns = [
    path('', views.list_meal_packages, name='list_meal_packages'),
    # You can add more URL patterns for this app here in the future
    # For example:
    # path('package/<int:pk>/', views.meal_package_detail, name='meal_package_detail'),
]