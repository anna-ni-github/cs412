from django.contrib import admin
from .models import ClothingItem, Outfit, OutfitItem

admin.site.register(ClothingItem)
admin.site.register(Outfit)
admin.site.register(OutfitItem)