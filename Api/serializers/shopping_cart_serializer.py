from rest_framework import serializers

from Api.serializers.photos_serializer import GetPhotosSerializer
from Api.serializers.user_serializer import UserSimpleSerializer
from Photos.models.shopping_cart import ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    # check the user serializers
    user = UserSimpleSerializer()
    photo = GetPhotosSerializer()

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        # depth goes within the relations
        depth = 1
