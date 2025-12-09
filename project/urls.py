#file: project/urls.py
#author: Anna Ni (annani@bu.edu)
#description: URL configuration for the Django project, routing to app-specific URLs.

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
    
    
    # ClothingItem URLs
    path('clothing/', views.ClothingItemListView.as_view(), name='clothing_list'),
    path('clothing/add/', views.ClothingItemCreateView.as_view(), name='clothing_add'),  # This line must be present!
    path('clothing/<int:pk>/', views.ClothingItemDetailView.as_view(), name='clothing_detail'),
    path('clothing/<int:pk>/edit/', views.ClothingItemUpdateView.as_view(), name='clothing_edit'),
    path('clothing/<int:pk>/delete/', views.ClothingItemDeleteView.as_view(), name='clothing_delete'),
    
    # Outfit URLs
    path('outfits/', views.OutfitListView.as_view(), name='outfit_list'),
    path('outfits/add/', views.OutfitCreateView.as_view(), name='outfit_add'),
    path('outfit/<int:pk>/', views.OutfitDetailView.as_view(), name='outfit_detail'),
    path('outfit/<int:pk>/edit/', views.OutfitUpdateView.as_view(), name='outfit_edit'),
    path('outfit/<int:pk>/delete/', views.OutfitDeleteView.as_view(), name='outfit_delete'),
    
    # OutfitItem URLs
    path('outfit/<int:outfit_id>/add-item/', views.OutfitItemCreateView.as_view(), name='outfititem_add'),
    path('outfititem/<int:pk>/delete/', views.OutfitItemDeleteView.as_view(), name='outfititem_delete'),

]