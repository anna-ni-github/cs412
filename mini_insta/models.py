"""
Author: Anna Ni
Email: annani@bu.edu
Course: CS412 - Django Project
File: models.py
Description: Defines the Profile model for the Mini Insta application, 
             including attributes such as username, display name, profile 
             image URL, bio text, and join date.
"""

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Profile(models.Model):
   #Represents a user profile in the Mini Insta application.
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=100)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        #   Return a string representation of the profile object.
        # Example: "anna (Anna Smith)"
        
        return f'{self.username} ({self.display_name})'
    def get_all_posts(self):
        return Post.objects.filter(profile=self).order_by('-timestamp')


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Post by {self.profile.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    # Accessor: get all Photos linked to this Post
    def get_all_photos(self):
        return Photo.objects.filter(post=self).order_by('timestamp')
    


class Photo(models.Model):
    # Each Photo belongs to one Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
    # Image is referenced by a public URL
    image_url = models.URLField()
    # Timestamp when photo was created
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Photo for {self.post.profile.username}'s post"