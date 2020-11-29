from django.db import models

from Photos.models.photos_model import Photos


class Wishes(models.Model):
    photo = models.ForeignKey(Photos, on_delete=models.CASCADE)
