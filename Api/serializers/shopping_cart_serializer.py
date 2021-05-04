from rest_framework import serializers
from Api.serializers.photos_serializer import ShowPhotosSerializer, SellPhotosSerializer
from Api.serializers.user_serializer import UserSimpleSerializer
from Photos.models.shopping_cart import ShoppingCart


class ShowShoppingCartSerializer(serializers.ModelSerializer):
    """
    Shows all fields for every Item in the Cart.
    Uses UserSimpleSerializer to get only the user id and username.
    Uses ShowPhotosSerializer to get all public fields for every Photo.
    depth = 1 shows all the data 1 relation deeper

    Suitable for getting all data for the Cart.
    """
    user = UserSimpleSerializer()
    photo = ShowPhotosSerializer()

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        depth = 1


class AddToShoppingCartSerializer(serializers.ModelSerializer):
    """
    Shows all fields for every Cart item without depth.
    To create or edit requires only User & Photo Id.

    Suitable for adding and removing from cart.
    """
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShowBoughtItemsSerializer(serializers.ModelSerializer):
    """
    Shows all Public & Private fields for every Item in the Cart.
    Uses UserSimpleSerializer to get only the user id and username.
    Uses SellPhotosSerializer to get all Public & Private fields for every Photo.
    depth = 1 shows all the data 1 relation deeper

    Suitable for getting all Bought Photos data.
    """
    user = UserSimpleSerializer()
    photo = SellPhotosSerializer()

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        depth = 1
