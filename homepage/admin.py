from django.contrib import admin
from django import forms

from homepage.models import Picture, Author, Album

class AuthorChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "Author: {}".format(obj.name)


class AlbumChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "Album: {}".format(obj.name)


class PictureAdmin(admin.ModelAdmin):
    list_display = ['id']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'album':
            return AlbumChoiceField(queryset=Album.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name',]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            return AuthorChoiceField(queryset=Author.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Picture, PictureAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Album, AlbumAdmin)