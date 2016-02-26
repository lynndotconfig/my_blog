from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.DurationField()
    podcast_id = models.IntegerField()


class MediaFile(models.Model):
    category = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    path = models.CharField(max_length=200)
