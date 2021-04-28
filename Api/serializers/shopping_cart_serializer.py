from rest_framework import serializers
from Api.serializers.photos_serializer import ShowPhotosSerializer, SellPhotosSerializer
from Api.serializers.user_serializer import UserSimpleSerializer
from Photos.models.shopping_cart import ShoppingCart


class ShowShoppingCartSerializer(serializers.ModelSerializer):
    # check the user serializers
    user = UserSimpleSerializer()
    photo = ShowPhotosSerializer()

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        # depth goes within the relations
        depth = 1


class AddToShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShowBoughtItemsSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer()
    photo = SellPhotosSerializer()

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        depth = 1
