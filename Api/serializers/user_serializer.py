from rest_framework import serializers

from Auth.models import UserProfile
from rest_framework.fields import CharField
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    extended = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

        # exclude = ('password', )
