from django.contrib.auth.models import User
from django.db import models

from Photos.models.photos_model import Photos


class Wishes(models.Model):
    photo = models.ForeignKey(Photos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
