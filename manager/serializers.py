from .models import Photo, Album
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['id']


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    album_id = AlbumSerializer(read_only=True)

    class Meta:
        model = Photo
        fields = [
            'id',
            'title',
            'album_id',
            'width',
            'height',
            'dominant_color',
            'url_local'
        ]
