from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
import requests
from manager.models import Photo
from manager.views import define_import_source
from manager.views import read_local_photo_file
from manager.views import import_from_external_api
from manager.views import import_from_json_file


class PhotoListApiTest(APITestCase):
    """
    Tests for api_view: 'photo_list'
    """
    def setUp(self):
        Photo.objects.create(
            title='example title',
            album_id='1',
            width=100,
            height=100,
            color_dominant='92c952',
            url='/example/url/photo.jpg'
        )
        self.url = 'http://127.0.0.1:8000/zdjecia'

    def test_get_all(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json = response.json()
        self.assertEqual(type(json), list)
        if json:
            self.assertEqual(type(json[0]), dict)

    def test_post_new(self):
        data = {
            "title": "apple",
            "album_id": 1,
            "url": 'manager/example_photos/apple.jpg'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        json = response.json()
        self.assertEqual(json['id'], 2)
        self.assertEqual(json['title'], 'apple')
        self.assertEqual(json['width'], 500)
        self.assertEqual(json['height'], 555)
        self.assertEqual(json['color_dominant'], '9ec23d')


class PhotoDetailApiTest(APITestCase):
    """
    Tests for api_view: 'photo_detail'
    """
    def setUp(self):
        Photo.objects.create(
            title='example title',
            album_id='1',
            width=100,
            height=100,
            color_dominant='92c952',
            url='/example/url/photo.jpg'
        )
        self.url = 'http://127.0.0.1:8000/zdjecia/1'

    def test_1_get_photo(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        global json
        json = response.json()
        self.assertEqual(type(json), dict)

    def test_2_put_photo(self):
        json['title'] = 'new different title'
        response_put = self.client.put(self.url, json, format='json')
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        response_get = self.client.get(self.url)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        title = response_get.json()['title']
        self.assertEqual(title, 'new different title')

    def test_3_delete_photo(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PhotoSourceTest(TestCase):
    """
    Tests for defining source of photo: local_photo_file, external_api, json_file.
    """

    def test_source_is_local_disk(self):
        url = '/home/user/example_dir/photo.jpg'
        source_type = define_import_source(url)
        self.assertEqual(source_type, 'local_photo_file')

    def test_source_is_external_api(self):
        url = 'https://via.placeholder.com/600/92c952'
        source_type = define_import_source(url)
        self.assertEqual(source_type, 'external_api')

    def test_source_is_json_file(self):
        url = '/home/user/photo_details.json'
        source_type = define_import_source(url)
        self.assertEqual(source_type, 'json_file')


class DetailsFromLocalPhotoFileTest(TestCase):
    def test_read_details_from_local_photo_file(self):
        self.url = 'manager/example_photos/strawberries.jpg'
        file_details = read_local_photo_file(self.url)
        width = file_details['width']
        height = file_details['height']
        color_dominant = file_details['color_dominant']

        self.assertEqual(width, 1350)
        self.assertEqual(height, 898)
        self.assertEqual(color_dominant, 'd01c23')


class DetailsFromExternalApiTest(TestCase):
    def test_read_details_from_external_api(self):
        self.url = 'https://jsonplaceholder.typicode.com/photos/1'
        photo_details = import_from_external_api(self.url)

        self.assertEqual(photo_details['height'], 600)
        self.assertEqual(photo_details['color_dominant'], '92c952')


class DetailsFromJsonFileTest(TestCase):
    def test_read_details_from_json_file(self):
        pass
