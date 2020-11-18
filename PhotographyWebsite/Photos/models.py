from django.db import models


# Create your models here.
class Photos(models.Model):
    original_photo = models.ImageField(upload_to='private/original_photos')
    watermarked_photo = models.ImageField(upload_to='public/photos')
    name = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=80, blank=False)
    price = models.IntegerField(blank=False)
    wishes = models.IntegerField(default=0)
