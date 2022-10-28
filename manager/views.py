from .models import Photo
from rest_framework import viewsets
from manager.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint to get info about all photos in the database
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
