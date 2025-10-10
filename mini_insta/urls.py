# mini_insta/urls.py
from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView, DeletePostView, PostUpdateView

app_name = 'mini_insta'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='show_profile'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='show_post'),
    path('profile/<int:pk>/create_post/', CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), 
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
]
