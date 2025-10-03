#File: views.py
#Author: Anna Ni (annani@bu.edu)
#Description: Implements views for displaying lists of profiles and details for individual profiles in the Mini Insta application.


from django.views.generic import ListView, DetailView
from .models import Profile, Post

class ProfileListView(ListView):
    #Display a list of all Profile objects.
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    # Display detailed information for a single Profile object.
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

class PostDetailView(DetailView):
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"
