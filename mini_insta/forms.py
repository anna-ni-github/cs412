#File: forms.py
#Author: Anna Ni (annani@bu.edu)
#Description: mini_insta/forms.py

from django import forms
from .models import Post
from .models import Profile

class CreatePostForm(forms.ModelForm):
    # extra field for Photo (since Photo is separate model)
    image_url = forms.URLField(required=False, label="Image URL")  # optional field

    class Meta:
        model = Post
        fields = ['caption', 'image_url' ]  # don't include profile (we set that in view)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']  # fields user can update