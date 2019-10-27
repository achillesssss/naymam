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
  author = models.TextField(blank=True, null=True)
  category = models.CharField(
        max_length=6,
        choices=TYPES_OF_PICTURE,
        default=SOIL,
    )
