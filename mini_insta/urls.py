# mini_insta/urls.py
from django.urls import path
from . import views
from .views import (
    ProfileListView, 
    ProfileDetailView, 
    PostDetailView, 
    CreatePostView, 
    UpdateProfileView, 
    CreateProfileView,
    DeletePostView, 
    PostUpdateView,
    ShowFollowersDetailView,
    ShowFollowingDetailView,
    PostFeedListView,
    SearchView,
    FollowProfileView,      
    UnfollowProfileView,    
    LikePostView,          
    UnlikePostView,         
)
from django.contrib.auth import views as auth_views


app_name = 'mini_insta'

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='show_profile'),
    path('profile/<int:pk>/feed', PostFeedListView.as_view(), name='show_feed'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='show_followers'),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='show_following'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='show_post'),
    path('profile/<int:pk>/create_post/', CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), 
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('profile/<int:pk>/search', SearchView.as_view(), name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='mini_insta/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_insta/logged_out.html'), name='logout'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    
    path('profile/<int:pk>/follow', FollowProfileView.as_view(), name='follow'),
    path('profile/<int:pk>/delete_follow', UnfollowProfileView.as_view(), name='unfollow'),
    
    path('post/<int:pk>/like', LikePostView.as_view(), name='like_post'),
    path('post/<int:pk>/delete_like', UnlikePostView.as_view(), name='unlike_post'),
    
    path('login/', auth_views.LoginView.as_view(template_name='mini_insta/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_insta/logged_out.html'), name='logout'),
    
]