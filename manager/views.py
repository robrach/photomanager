from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view

import requests
import json

from manager.models import Photo
from manager.serializers import PhotoSerializer

from colorthief import ColorThief
from PIL import Image


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
        print("\n...log from api.view.photo_list -> request.method=='POST':")
        print("...data in post request:", photo_data)

        url = photo_data['url']
        import_source = define_import_source(url)
        print('...IMPORT SOURCE:', import_source)

        if import_source == 'local_photo_file':
            data_import = read_local_photo_file(url)
            photo_data['width'] = data_import['width']
            photo_data['height'] = data_import['height']
            photo_data['color_dominant'] = data_import['color_dominant']
        elif import_source == 'external_api':
            data_import = import_from_external_api(url)
            define_photo_data(photo_data, data_import)
        elif import_source == 'json_file':
            data_import = import_from_json_file(url)
            define_photo_data(photo_data, data_import)

        photo_serializer = PhotoSerializer(data=photo_data)

        if photo_serializer.is_valid():
            photo_serializer.save()
            print("...response data after post:", photo_serializer.data)
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


def define_import_source(url):
    """
    Return type of source: local_photo_file OR external_api OR json_file.
    """
    if url[:4] == 'http':
        return 'external_api'
    elif url[-5:] == '.json':
        return 'json_file'
    else:
        return 'local_photo_file'


def read_local_photo_file(url):
    image = Image.open(url)
    width = image.width
    height = image.height

    color_thief = ColorThief(url)
    dominant_color_rgb = color_thief.get_color(quality=1)
    dominant_color_hex = '%02x%02x%02x' % dominant_color_rgb
    return {
        'width': width,
        'height': height,
        'color_dominant': dominant_color_hex,
    }


def import_from_external_api(url):
    response = requests.get(url)
    data = response.json()
    return dict_from_data(data)


def import_from_json_file(url):
    file = open(url)
    data = json.load(file)
    return dict_from_data(data)


def dict_from_data(data):
    title = data['title']
    album_id = data['albumId']
    url = data['url']
    splitted_url = url.split('/')
    width = int(splitted_url[-2])
    height = int(splitted_url[-2])
    color_dominant = splitted_url[-1]
    return {
        'title': title,
        'album_id': album_id,
        'url': url,
        'width': width,
        'height': height,
        'color_dominant': color_dominant,
    }


def define_photo_data(photo_data, data_import):
    photo_data['title'] = data_import['title']
    photo_data['album_id'] = data_import['album_id']
    photo_data['url'] = data_import['url']
    photo_data['width'] = data_import['width']
    photo_data['height'] = data_import['height']
    photo_data['color_dominant'] = data_import['color_dominant']
    return photo_data
