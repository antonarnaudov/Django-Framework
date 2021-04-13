from django.contrib import admin

# Register your models here.
from Auth.models import UserProfile

admin.site.register(UserProfile)
