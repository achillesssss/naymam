from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from homepage.models import Picture

def picture_to_json(picture):
  return {
    'url': picture.photo.url,
    'description': picture.description,
    'author': picture.author
  }

def index(request):
  pictures = Picture.objects.all()
  picture_data = []
  for picture in pictures:
    picture_data.append(picture_to_json(picture))
  return render(request, 'index.html', {'pictures': picture_data})