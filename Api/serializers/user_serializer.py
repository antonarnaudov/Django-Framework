from rest_framework import serializers
from Auth.models import UserProfile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    Shows all fields for the extended user Profile.

    Suitable for showing only the Extended User fields.
    """
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Shows all fields for the User & UserProfile.

    Suitable for showing all User fields Default and Custom.
    """
    extended = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined')


class UserSimpleSerializer(serializers.ModelSerializer):
    """
    Shows only id and username fields of the user.

    Suitable usage in other serializers where you dont need all the user data.
    """
    class Meta:
        model = User
        fields = ('id', 'username')
