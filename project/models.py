#file: project/models.py
#author: Anna Ni (annani@bu.edu)
#description: Models for managing clothing items and outfits in the Django final project.

from django.db import models
from django.contrib.auth.models import User

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('tops', 'Tops'),
        ('bottoms', 'Bottoms'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
        ('outerwear', 'Outerwear'),
    ]
    
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
        ('all-season', 'All Season'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=50)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES)
    brand = models.CharField(max_length=100, blank=True)
    image_url = models.URLField()
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.category})"

class Outfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)
    outfit_url = models.URLField()  # Just a link to the outfit image/inspo
    date_created = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class OutfitItem(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.clothing_item.name} in {self.outfit.name}"