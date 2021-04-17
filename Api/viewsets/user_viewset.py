from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from Api.serializers.user_serializer import UserSerializer
from Auth.models import UserProfile


# class UserListApiView(ListAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserSerializer


class UserListApiView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)
