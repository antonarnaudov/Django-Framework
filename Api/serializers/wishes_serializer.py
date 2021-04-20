from rest_framework import serializers

from Api.serializers.photos_serializer import PhotosSerializer
from Api.serializers.user_serializer import UserSimpleSerializer
from Photos.models.wishes_model import Wishes


class WishesSerializer(serializers.ModelSerializer):
    # check the user serializers
    user = UserSimpleSerializer()
    photo = PhotosSerializer()

    class Meta:
        model = Wishes
        fields = '__all__'
        # depth goes within the relations
        depth = 1
