from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view


from .models import Photo
from manager.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint to get info about all photos in the database
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


@api_view(['GET', 'POST'])
def photo_list(request):
    # GET list of photos, POST a new photo
    if request.method == 'GET':
        photos = Photo.objects.all()

        photos_serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(photos_serializer.data, safe=False)

    elif request.method == 'POST':
        photo_data = JSONParser().parse(request)
        # In the request only tile, album_id, url_local are given, so below other values are defined
        photo_data['width'] = 9999  # TODO: here call the function that will define the value
        photo_data['height'] = 9999 # TODO: here call the function that will define the value
        photo_data['dominant_color'] = '9999'   # TODO: here call the function that will define the value
        photo_serializer = PhotoSerializer(data=photo_data)
        if photo_serializer.is_valid():
            photo_serializer.save()
            return JsonResponse(photo_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def photo_detail(request, pk):
    # find photo by pk (id)
    # GET / PUT / DELETE photo
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return JsonResponse({'message': f'The photo id={pk} does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        photo_serializer = PhotoSerializer(photo)
        return JsonResponse(photo_serializer.data)

    elif request.method == 'PUT':
        photo_data = JSONParser().parse(request)
        photo_serializer = PhotoSerializer(photo, data=photo_data)
        if photo_serializer.is_valid():
            photo_serializer.save()
            return JsonResponse(photo_serializer.data)
        return JsonResponse(photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        photo.delete()
        return JsonResponse({'message': f'Photo id={pk} was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
