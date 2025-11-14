# dadjokes/urls.py
from django.urls import path
from . import views, api_views  

urlpatterns = [
    path('', views.index, name='index'),
    path('random/', views.random_view, name='random'),
    path('jokes/', views.all_jokes, name='jokes'),
    path('joke/<int:pk>/', views.joke_detail, name='joke_detail'),
    path('pictures/', views.all_pictures, name='pictures'),
    path('picture/<int:pk>/', views.picture_detail, name='picture_detail'),

    # API endpoints
    path('api/', api_views.random_joke),
    path('api/random/', api_views.random_joke),
    path('api/jokes/', api_views.jokes_list),
    path('api/joke/<int:pk>/', api_views.joke_detail),
    path('api/pictures/', api_views.pictures_list),
    path('api/picture/<int:pk>/', api_views.picture_detail),
    path('api/random_picture/', api_views.random_picture),
]
