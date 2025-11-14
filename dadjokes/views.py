from django.shortcuts import render, get_object_or_404
from .models import Joke, Picture
import random

def index(request):
    joke = random.choice(Joke.objects.all())
    picture = random.choice(Picture.objects.all())
    return render(request, 'dadjokes/index.html', {'joke': joke, 'picture': picture})

def random_view(request):
    return index(request)

def all_jokes(request):
    jokes = Joke.objects.all()
    return render(request, 'dadjokes/jokes.html', {'jokes': jokes})

def joke_detail(request, pk):
    joke = get_object_or_404(Joke, pk=pk)
    return render(request, 'dadjokes/joke_detail.html', {'joke': joke})

def all_pictures(request):
    pictures = Picture.objects.all()
    return render(request, 'dadjokes/pictures.html', {'pictures': pictures})

def picture_detail(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    return render(request, 'dadjokes/picture_detail.html', {'picture': picture})
