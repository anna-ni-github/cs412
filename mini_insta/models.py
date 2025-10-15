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
from django.views.generic import UpdateView


class Profile(models.Model):
   #Represents a user profile in the Mini Insta application.
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=100)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        # Return a string representation of the profile object.
        # Example: "anna (Anna Smith)"
        
        return f'{self.username} ({self.display_name})'
    def get_all_posts(self):
        return Post.objects.filter(profile=self).order_by('-timestamp')
    
    def get_absolute_url(self):
        return reverse('mini_insta:show_profile', kwargs={'pk': self.pk})
    
    def get_followers(self):
        #Return list of Profiles who follow this Profile.
        followers = Follow.objects.filter(profile=self)
        return [f.follower_profile for f in followers]

    def get_num_followers(self):
        #Return the number of followers
        return Follow.objects.filter(profile=self).count()

    def get_following(self):
        #Return list of Profiles this Profile follows.
        following = Follow.objects.filter(follower_profile=self)
        return [f.profile for f in following]
    
    def get_post_feed(self):
    #Return a QuerySet of Posts from all profiles that this Profile is following.
    #Posts are ordered by timestamp (most recent first).
    
        # Get all profiles this Profile is following
        following = self.get_following()
        
        # Get all posts from those profiles
        # Use the 'in' lookup to find posts where the profile is in the following list
        posts = Post.objects.filter(profile__in=following).order_by('-timestamp')
        
        return posts

    def get_num_following(self):
        #Return the number of Profiles this Profile follows.
        return Follow.objects.filter(follower_profile=self).count()
    
    


class Post(models.Model):
    #represents a post made by a user profile in the Mini Insta application.
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return f"Post by {self.profile.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
    def get_all_photos(self):
        return Photo.objects.filter(post=self).order_by('timestamp')
    
    def get_all_comments(self):
        return Comment.objects.filter(post=self).order_by('-timestamp')

    def get_likes(self):
        return Like.objects.filter(post=self)

    def get_num_likes(self):
        return Like.objects.filter(post=self).count()


class Photo(models.Model):
    # Represents a photo associated with a post in the Mini Insta application.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def get_image_url(self):
        
        #Return a usable URL for this photo:
     
        if self.image_url:
            return self.image_url
        if self.image_file:
            try:
                return self.image_file.url
            except ValueError:
                return None
        return None

    def __str__(self):
        # reflect how the image is stored
        if self.image_url:
            return f"Photo (URL) for post {self.post.pk}"
        if self.image_file:
            return f"Photo (file) for post {self.post.pk}"
        return f"Photo (no image) for post {self.post.pk}"

class UpdatePostView(UpdateView):
    # Allow users to update the caption of an existing Post.
    model = Post
    fields = ['caption']
    template_name = 'mini_insta/update_post_form.html'

    def get_success_url(self):
        return reverse('mini_insta:show_post', kwargs={'pk': self.object.pk})
    
# Add these to your models.py - replace the existing __str__ methods

class Follow(models.Model):
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name="profile"  # the one being followed
    )
    follower_profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name="follower_profile"  # the one following
    )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Fixed: use username directly, not user.username
        return f"{self.follower_profile.username} follows {self.profile.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Fixed: use username directly
        return f"{self.profile.username} commented on {self.post}: {self.text[:30]}..."


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Fixed: use username directly
        return f"{self.profile.username} liked {self.post}"  
    
