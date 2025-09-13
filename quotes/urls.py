from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.quote, name='quote'),          # /quotes/
    path(r'quote/', views.quote, name='quote'),    # /quotes/quote/
    path(r'show_all/', views.show_all, name='show_all'),  # /quotes/show_all/
    path(r'about/', views.about, name='about'),    # /quotes/about/
]
