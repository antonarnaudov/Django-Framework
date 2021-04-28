from rest_framework import serializers
from Photos.models.category_model import Category


class ShowCategorySerializer(serializers.ModelSerializer):
    """
    Shows All fields for Category.

    Suitable for showing in a List
    """
    class Meta:
        model = Category
        fields = '__all__'


class UpdateCategorySerializer(serializers.ModelSerializer):
    """
    Shows All fields for Category.
    Makes image field Not required.

    Suitable for Updating.
    """
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'image': {'required': False}}


class SimpleCategorySerializer(serializers.ModelSerializer):
    """
    Shows just the Category field.

    Suitable for usage in other Serializers,
    where the Image is not needed.
    """
    class Meta:
        model = Category
        fields = ('category', )
