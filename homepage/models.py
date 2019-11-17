from django.db import models


class Picture(models.Model):
  SOIL = 'soil'
  WATER = 'water'
  AIR = 'air'
  LIGHT = 'light'
  TYPES_OF_PICTURE = [
    (SOIL, 'Soil'),
    (WATER, 'Water'),
    (AIR, 'Air'),
    (LIGHT, 'Light'),
  ]
  photo = models.ImageField(upload_to='static/', blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  album = models.ForeignKey('Album', on_delete=models.CASCADE, default=1, related_name='pictures')
  category = models.CharField(
      max_length=6,
      choices=TYPES_OF_PICTURE,
      default=SOIL,
  )


class Album(models.Model):
  name = models.TextField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):
  name = models.TextField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  link = models.TextField(blank=True, null=True)

