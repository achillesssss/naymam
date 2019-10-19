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
  picture_data1 = []
  picture_data2 = []
  picture_data3 = []
  turn = 1
  for picture in pictures:
    if turn % 3 == 1:
      picture_data1.append(picture_to_json(picture))
    elif turn % 3 == 2:
      picture_data2.append(picture_to_json(picture))
    elif turn % 3 == 0:
      picture_data3.append(picture_to_json(picture))
    turn += 1
  return render(request, 'index.html', {
    'pictures1': picture_data1,
    'pictures2': picture_data2,
    'pictures3': picture_data3
  })