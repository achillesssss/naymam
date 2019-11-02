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
  category = request.GET.get('category')
  pictures = Picture.objects.all()
  if category:
    if category != 'all':
      pictures = pictures.filter(category=category)
  picture_data1 = []
  picture_data2 = []
  picture_data3 = []
  mobile_1 = []
  mobile_2 = []
  turn = 1
  for picture in pictures:
    if turn % 2 == 1:
      mobile_1.append(picture_to_json(picture))
    else:
      mobile_2.append(picture_to_json(picture))
    if turn % 3 == 1:
      picture_data1.append(picture_to_json(picture))
    elif turn % 3 == 2:
      picture_data2.append(picture_to_json(picture))
    elif turn % 3 == 0:
      picture_data3.append(picture_to_json(picture))
    turn += 1

  return render(request, 'index.html', {
    'pictures1': picture_data1,
    'pictures1_mobile': mobile_1,
    'pictures2_mobile': mobile_2,
    'pictures2': picture_data2,
    'pictures3': picture_data3
  })