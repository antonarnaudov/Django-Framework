from django.contrib import admin

# Register your models here.
from Photos.models.category_model import Category
from Photos.models.photos_model import Photos
from Photos.models.shopping_cart import ShoppingCart
from Photos.models.wishes_model import Wishes

admin.site.register(Photos)
admin.site.register(Category)
admin.site.register(Wishes)
admin.site.register(ShoppingCart)
