from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Joke, Picture
from .serializers import JokeSerializer, PictureSerializer
import random

@api_view(['GET'])
def random_joke(request):
    joke = random.choice(Joke.objects.all())
    return Response(JokeSerializer(joke).data)

@api_view(['GET', 'POST'])
def jokes_list(request):
    if request.method == 'GET':
        jokes = Joke.objects.all()
        return Response(JokeSerializer(jokes, many=True).data)
    elif request.method == 'POST':
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def joke_detail(request, pk):
    try:
        joke = Joke.objects.get(pk=pk)
    except Joke.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(JokeSerializer(joke).data)

@api_view(['GET'])
def pictures_list(request):
    pictures = Picture.objects.all()
    return Response(PictureSerializer(pictures, many=True).data)

@api_view(['GET'])
def picture_detail(request, pk):
    try:
        picture = Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(PictureSerializer(picture).data)

@api_view(['GET'])
def random_picture(request):
    picture = random.choice(Picture.objects.all())
    return Response(PictureSerializer(picture).data)
