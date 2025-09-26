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

class Profile(models.Model):
    """
    Represents a user profile in the Mini Insta application.

    Attributes:
        username (CharField): Unique username for the profile.
        display_name (CharField): Display name shown publicly.
        profile_image_url (URLField): URL pointing to the profile image.
        bio_text (TextField): Short biography text for the profile.
        join_date (DateField): Date the user joined, auto-generated.
    """
    username = models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=100)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the profile object.

        Returns:
            str: A string showing the username and display name.
        """
        return f'{self.username} ({self.display_name})'
