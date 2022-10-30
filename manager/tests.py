from django.test import TestCase
from rest_framework import status
import requests
from manager.views import define_import_source


class PhotoListApiTest(TestCase):
    """
    Tests for api_view 'photo_list'
    """
    def test_get_all(self):
        response = requests.get('http://127.0.0.1:8000/zdjecia')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json = response.json()
        self.assertEqual(type(json), list)
        if json:
            self.assertEqual(type(json[0]), dict)

    def test_post_new(self):
        content = {
            "title": "example title",
            "album_id": 1,
            "url": "/example/url/sting"
        }
        response = requests.post('http://127.0.0.1:8000/zdjecia', json=content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        json = response.json()
        title = json['title']
        self.assertEqual(title, 'example title')


class PhotosDetailApiTest(TestCase):
    """
    Tests for api_view 'photo_detail'
    """
    def test_1_get_photo(self):
        response = requests.get('http://127.0.0.1:8000/zdjecia')
        global id
        id = (response.json()[-1]['id'])
        response = requests.get(f'http://127.0.0.1:8000/zdjecia/{id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        global json
        json = response.json()
        self.assertEqual(type(json), dict)

    def test_2_put_photo(self):
        json['title'] = 'new different title'
        response_put = requests.put(f'http://127.0.0.1:8000/zdjecia/{id}', json=json)
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        response_get = requests.get(f'http://127.0.0.1:8000/zdjecia/{id}')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

        title = response_get.json()['title']
        self.assertEqual(title, 'new different title')

    def test_3_delete_photo(self):
        response = requests.delete(f'http://127.0.0.1:8000/zdjecia/{id}')
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
