from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to='public/category_photos')
    category = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.category
