from .models import Photo, Album
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'id',
            'title',
            'album_id',
            'width',
            'height',
            'color_dominant',
            'url'
        ]
