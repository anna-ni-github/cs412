#cs412/urls.py
#author: Anna Ni (annani@bu.edu)
#description: Main URL configuration for the cs412 project, routing to various apps including voter_analytics.

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('quotes/', include('quotes.urls')),
    path('restaurant/', include('restaurant.urls')),  
    path('mini_insta/', include('mini_insta.urls')),
    path('voter_analytics/', include('voter_analytics.urls')), 
    path('dadjokes/', include('dadjokes.urls')), 
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('project/', include('project.urls')), #NEW
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)