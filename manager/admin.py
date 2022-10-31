from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'id',
        'title',
        'album_id',
        'width',
        'height',
        'color_dominant',
        'url',
    ]
