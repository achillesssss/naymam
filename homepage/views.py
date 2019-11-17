from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.db.models import Prefetch

from homepage.models import Picture, Album, Author

def picture_to_json(picture):
  return {
    'url': picture.photo.url,
    'description': picture.description,
    'author': picture.album.author.name
  }

def album_to_json(album):
  return {
    'id': album.id,
    'name': album.name,
    'description': album.description,
    'author': {
      'name': album.author.name,
      'description': album.author.description,
      'link': album.author.link,
    },
    'pictures': [picture_to_json(picture) for picture in album.real_pictures]
  }

def index(request):
  category = request.GET.get('category')
  albums = Album.objects.all().select_related('author').prefetch_related(
    Prefetch('pictures', queryset=Picture.objects.all(), to_attr='real_pictures')
  )

  if category:
    if category != 'all':
      pictures = pictures.filter(category=category)
  picture_data1 = []
  picture_data2 = []
  picture_data3 = []
  mobile_1 = []
  mobile_2 = []
  turn = 1
  albums_json = []
  count = 0
  for album in albums:
    if len(album.real_pictures):
      albums_json.append(album_to_json(album))
      count += 1

  for album in albums_json:
      picture = album['pictures'][0]
      item = {
        'count': count,
        'id': album['id'],
        'picture': picture,
        'showcase': album
      }
      if turn % 2 == 1:
        mobile_1.append(item)
      else:
        mobile_2.append((item))
      if turn % 3 == 1:
        picture_data1.append((item))
      elif turn % 3 == 2:
        picture_data2.append((item))
      elif turn % 3 == 0:
        picture_data3.append((item))
      turn += 1

  # import pdb; pdb.set_trace()
  return render(request, 'index.html', {
    'pictures1': picture_data1,
    'pictures1_mobile': mobile_1,
    'pictures2_mobile': mobile_2,
    'pictures2': picture_data2,
    'pictures3': picture_data3
  })