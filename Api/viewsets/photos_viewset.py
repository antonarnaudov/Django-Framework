from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Api.serializers.photos_serializer import ShowPhotosSerializer, CreatePhotoSerializer, UpdatePhotoSerializer
from Photos.models.photos_model import Photos
from common_functionality.custom_filter_classes import PhotosFilter
from common_functionality.mixins import SerializerRequestSwitchMixin


# @parser_classes((FormParser, MultiPartParser))
class PhotosViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    """
    ViewSet supporting all operations for Photos.
    """
    queryset = Photos.objects.all()

    serializers = {
        'show': ShowPhotosSerializer,
        'create': CreatePhotoSerializer,
        'update': UpdatePhotoSerializer
    }

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filter_class = PhotosFilter

    search_fields = ('name',)
    ordering_fields = ('price',)
    ordering = 'price'
