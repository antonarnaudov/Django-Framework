from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.serializers.photos_serializer import PhotosSerializer
from Photos.models.photos_model import Photos


class PhotosPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 100


class PhotosListApiView(ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('price', )
    search_fields = ('name', )
    pagination_class = PhotosPagination
