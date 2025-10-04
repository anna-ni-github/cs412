# mini_insta/urls.py
from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView

app_name = 'mini_insta'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='show_profile'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='show_post'),
    path('profile/<int:pk>/create_post/', CreatePostView.as_view(), name='create_post'),
]
