from rest_framework import serializers
from Photos.models.photos_model import Photos


class ShowPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('original_photo', )


class CreatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('watermarked_photo', )


class UpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('watermarked_photo', )
        extra_kwargs = {'original_photo': {'required': False}}
