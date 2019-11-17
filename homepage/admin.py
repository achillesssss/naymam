from django.contrib import admin
from homepage.models import Picture, Author, Album

class PictureAdmin(admin.ModelAdmin):
    pass


class AlbumAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picture, PictureAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Album, AlbumAdmin)