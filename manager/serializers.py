from .models import Photo, Album
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'id',
            'title',
            # 'album_id',
            'width',
            'height',
            'dominant_color',
            'url_local'
        ]
        # extra_kwargs = {
        #     'album_id': {view_name}
        # }


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['id', '__str__']
