from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, CursorPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.serializers.photos_serializer import PhotosSerializer
from Photos.models.photos_model import Photos
from common_functionality.pagination_classes import CursorPaginationSettings


class PhotosListApiView(ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = ('price', )
    search_fields = ('name', )
    ordering_fields = ('price', )
    ordering = 'price'
    pagination_class = CursorPaginationSettings
