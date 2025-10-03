# mini_insta/urls.py
from django.urls import path
from . import views
from .views import ProfileDetailView, PostDetailView

app_name = 'mini_insta'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='show_profile'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='show_post')
]
