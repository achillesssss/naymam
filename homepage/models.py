from django.db import models


class Picture(models.Model):
  photo = models.ImageField(upload_to='static/', blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  author = models.TextField(blank=True, null=True)