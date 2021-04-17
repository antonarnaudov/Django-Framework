from rest_framework import serializers

from Photos.models.photos_model import Photos


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('original_photo', )
