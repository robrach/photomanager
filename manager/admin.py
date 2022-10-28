from django.contrib import admin
from .models import Album, Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'id',
        '__str__',
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'id',
        'title',
        'album_id',
        'width',
        'height',
        'dominant_color',
        'url_local',
    ]
