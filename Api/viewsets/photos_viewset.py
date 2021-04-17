from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.serializers.photos_serializer import PhotosSerializer
from Photos.models.photos_model import Photos


class PhotosListApiView(ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
