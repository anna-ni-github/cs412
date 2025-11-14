from django.db import models

class Joke(models.Model):
    """Model to store dad jokes"""
    text = models.TextField()
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text[:50]}... by {self.name}"
    
    class Meta:
        ordering = ['-timestamp']


class Picture(models.Model):
    """Model to store silly images/GIFs"""
    image_url = models.URLField(max_length=500)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Picture by {self.name}"
    
    class Meta:
        ordering = ['-timestamp']