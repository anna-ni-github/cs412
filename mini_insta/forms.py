# File: forms.py
# Author: Anna Ni (annani@bu.edu)
# Description: mini_insta/forms.py

from django import forms
from .models import Post, Profile

class CreatePostForm(forms.ModelForm):
    # Field for URL-based images (optional)
    post_image_url = forms.URLField(required=False, label="Image URL (optional)")  # CHANGED: image_url to post_image_url
    
    # Remove the files field from the form entirely
    # We'll handle file uploads directly in the view

    class Meta:
        model = Post
        fields = ['caption']  # Only caption from Post model

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']
        
class CreateProfileForm(forms.ModelForm):
    """Form to create a new Profile."""
    class Meta:
        model = Profile
        fields = ['username', 'display_name', 'bio_text', 'profile_image_url']