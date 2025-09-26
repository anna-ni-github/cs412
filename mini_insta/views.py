"""
Author: Anna Ni
Email: annani@bu.edu
Course: CS412 - Django Project
File: views.py
Description: Implements views for displaying lists of profiles and 
             details for individual profiles in the Mini Insta application.
"""

from django.views.generic import ListView, DetailView
from .models import Profile

class ProfileListView(ListView):
    """
    Display a list of all Profile objects.

    Inherits from:
        ListView (Django generic class-based view).

    Attributes:
        model (Profile): The data model to query.
        template_name (str): The path to the template used for rendering.
        context_object_name (str): The name of the context variable in the template.
    """
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    """
    Display details for a single Profile object.

    Inherits from:
        DetailView (Django generic class-based view).

    Attributes:
        model (Profile): The data model to query.
        template_name (str): The path to the template used for rendering.
        context_object_name (str): The name of the context variable in the template.
    """
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'
