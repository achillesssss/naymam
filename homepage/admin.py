from django.contrib import admin
from homepage.models import Picture

class PictureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picture, PictureAdmin)