from django.db import models


class Album(models.Model):

    def __str__(self):
        return f'Album_{self.pk}'


class Photo(models.Model):
    title = models.CharField(max_length=100)
    album_id = models.ForeignKey(Album, on_delete=models.PROTECT)
    width = models.IntegerField()
    height = models.IntegerField()
    dominant_color = models.CharField(max_length=10)
    url_local = models.CharField(max_length=255)

    def __str__(self):
        return f'Photo_{self.pk}'
