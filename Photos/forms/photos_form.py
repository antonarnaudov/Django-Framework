from django import forms

from Photos.models.photos_model import Photos


class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['original_photo', 'name', 'category', 'price']


