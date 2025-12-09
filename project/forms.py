#file: project/forms.py
#author: Anna Ni (annani@bu.edu)
#description: Forms for managing clothing items and outfits in the Django final project.

from django import forms
from .models import ClothingItem, Outfit, OutfitItem

# Form for adding/editing ClothingItem
class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ['name', 'category', 'color', 'season', 'brand', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Blue Denim Jacket'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'color': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Blue'}),
            'season': forms.Select(attrs={'class': 'form-input'}),
            'brand': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Levi\'s (optional)'}),
            'image_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://example.com/image.jpg'}),
        }

# Form for adding/editing Outfit
class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['name', 'occasion', 'outfit_url', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Casual Friday'}),
            'occasion': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Work, Date Night'}),
            'outfit_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://example.com/outfit.jpg'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Notes about this outfit...'}),
        }
       
# Form for adding OutfitItem (linking ClothingItem to Outfit) 
class OutfitItemForm(forms.ModelForm):
    class Meta:
        model = OutfitItem
        fields = ['clothing_item']
        widgets = {
            'clothing_item': forms.Select(attrs={'class': 'form-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Only show clothing items belonging to the current user
            self.fields['clothing_item'].queryset = ClothingItem.objects.filter(user=user)
            self.fields['clothing_item'].label = "Select a clothing item from your wardrobe"