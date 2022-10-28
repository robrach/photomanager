from .models import Photo, Album
from rest_framework import viewsets
from manager.serializers import PhotoSerializer, AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint to get info about all photos in the database
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
