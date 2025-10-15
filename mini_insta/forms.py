# File: forms.py
# Author: Anna Ni (annani@bu.edu)
# Description: mini_insta/forms.py

from django import forms
from .models import Post, Profile

class CreatePostForm(forms.ModelForm):
    # Field for URL-based images (optional)
    image_url = forms.URLField(required=False, label="Image URL (optional)")
    
    # Remove the files field from the form entirely
    # We'll handle file uploads directly in the view

    class Meta:
        model = Post
        fields = ['caption']  # Only caption from Post model

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']