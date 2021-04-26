from rest_framework import serializers

from Photos.models.photos_model import Photos


class GetPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('original_photo', )


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('watermarked_photo', )


class PutPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        exclude = ('watermarked_photo', )
        extra_kwargs = {'original_photo': {'required': False}}
