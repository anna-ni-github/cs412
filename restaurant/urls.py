from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),               # /restaurant/main/
    path('order/', views.order, name='order'),            # /restaurant/order/
    path('confirmation/', views.confirmation, name='confirmation'),  # /restaurant/confirmation/
]

