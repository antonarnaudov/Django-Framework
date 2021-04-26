from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Api.serializers.photos_serializer import GetPhotosSerializer, PostPhotoSerializer, PutPhotoSerializer
from Photos.models.photos_model import Photos
from common_functionality.custom_filter_classes import PhotosFilter
from common_functionality.pagination_classes import CursorPaginationSettings


class PhotosViewSet(ModelViewSet):
    """
    ViewSet supporting all operations for Photos.
    """
    queryset = Photos.objects.all()

    serializers = {
        'get': GetPhotosSerializer,
        'post': PostPhotoSerializer,
        'put': PutPhotoSerializer
    }

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filter_class = PhotosFilter
    pagination_class = CursorPaginationSettings

    search_fields = ('name',)
    ordering_fields = ('price',)
    ordering = 'price'

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.serializers['get']

        elif self.action == 'update':
            return self.serializers['put']

        return self.serializers['post']
