from rest_framework import serializers
from .models import Joke, Picture


class JokeSerializer(serializers.ModelSerializer):
    """Serializer for Joke model"""
    class Meta:
        model = Joke
        fields = ['id', 'text', 'name', 'timestamp']  # Use 'name' not 'contributor'
        read_only_fields = ['id', 'timestamp']


class PictureSerializer(serializers.ModelSerializer):
    """Serializer for Picture model"""
    class Meta:
        model = Picture
        fields = ['id', 'image_url', 'name', 'timestamp']  # Use 'name' not 'contributor'
        read_only_fields = ['id', 'timestamp']