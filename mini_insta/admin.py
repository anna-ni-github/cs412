# mini_insta/admin.py
from django.contrib import admin
from .models import Profile, Post, Photo

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'join_date')
    search_fields = ('username', 'display_name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'timestamp', 'caption')
    search_fields = ('profile__username', 'caption')
    list_filter = ('timestamp',)
    
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('post', 'image_url', 'timestamp')
    search_fields = ('post__profile__username',)
    list_filter = ('timestamp',)