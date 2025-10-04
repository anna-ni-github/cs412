#File: forms.py
#Author: Anna Ni (annani@bu.edu)
#Description: mini_insta/forms.py

from django import forms
from .models import * 

class CreatePostForm(forms.ModelForm):
    # extra field for Photo (since Photo is separate model)
    image_url = forms.URLField(required=False, label="Image URL")  # optional field

    class Meta:
        model = Post
        fields = ["caption"]  # don't include profile (we set that in view)
