#cs412/urls.py
#author: Anna Ni (annani@bu.edu)
#description: Main URL configuration for the cs412 project, routing to various apps including voter_analytics.
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('quotes/', include('quotes.urls')),
    path('restaurant/', include('restaurant.urls')),  
    path('mini_insta/', include('mini_insta.urls')),
    path('voter_analytics/', include('voter_analytics.urls')), #NEW
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)