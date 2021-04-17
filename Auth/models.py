# If extension to the User is needed this is the correct way to do it

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    # date_of_birth = models.DateField(blank=False)
    # image = models.ImageField(upload_to='profiles/')
    user = models.OneToOneField(User, related_name="extended", on_delete=models.CASCADE)
    # class Meta:
    #     proxy = True
    #     exclude = ('password', '')
