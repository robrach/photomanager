from django.db import models


class Album(models.Model):

    def __str__(self):
        return f'Album_{self.pk}'


class Photo(models.Model):
    title = models.CharField(max_length=100)
    album_id = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    color_dominant = models.CharField(max_length=10)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f'Photo_{self.pk}'
