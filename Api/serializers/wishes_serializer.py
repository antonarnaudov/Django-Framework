from rest_framework import serializers

from Api.serializers.photos_serializer import ShowPhotosForWishesSerializer
from Api.serializers.user_serializer import UserSimpleSerializer
from Photos.models.wishes_model import Wishes


class ShowWishesSerializer(serializers.ModelSerializer):
    """
    Shows all fields for every Wish.
    Uses UserSimpleSerializer to take only the user id and username.
    Uses ShowPhotosForWishesSerializer to get Photo public fields necessary for the Wishes.
    depth = 1 shows all the data 1 relation deeper

    Suitable for getting all data for the Wishes.
    """
    user = UserSimpleSerializer(help_text='user serializer')
    photo = ShowPhotosForWishesSerializer(help_text='photo serializer')

    class Meta:
        model = Wishes
        fields = '__all__'
        depth = 1


class CreateWishesSerializer(serializers.ModelSerializer):
    """
    Shows all fields for every Wish without depth.
    To create or edit requires only User & Photo Id.

    Suitable for creating and editing Wishes.
    """
    class Meta:
        model = Wishes
        fields = '__all__'
