from io import BytesIO

import numpy as np
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models

# Create your models here.
from Photos.common_functionality.watermarked_image_creator import create_watermarked_image
from Photos.models.category_model import Category


class Photos(models.Model):
    original_photo = models.ImageField(upload_to='private/original_photos')
    watermarked_photo = models.ImageField(upload_to='public/photos', blank=True)

    name = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.IntegerField(blank=False)

    def save(self, *args, **kwargs):
        pil_img = Image.open(self.original_photo)
        cv_img = np.array(pil_img)
        img = create_watermarked_image(cv_img)

        im_pil = Image.fromarray(img)

        buffer = BytesIO()
        im_pil.save(buffer, format='jpeg')

        image = buffer.getvalue()

        file_name = f'watermarked_{self.name.lower()}.jpeg'

        self.watermarked_photo.save(file_name, ContentFile(image), save=False)

        super().save(*args, **kwargs)
