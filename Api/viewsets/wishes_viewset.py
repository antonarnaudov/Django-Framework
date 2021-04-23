from django.core.exceptions import FieldDoesNotExist
from django.db.models import ForeignObjectRel, OneToOneRel
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.serializers.category_serializer import CategorySerializer
from Api.serializers.wishes_serializer import WishesSerializer
from Photos.models.photos_model import Photos
from Photos.models.wishes_model import Wishes
from common_functionality.pagination_classes import CursorPaginationSettings

# NOTE: ordering_fields does NOT support nested fields


class WishesListApiView(ListAPIView):
    serializer_class = WishesSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('photo__name',)
    ordering_fields = ''
    ordering = 'photo_id'
    pagination_class = CursorPaginationSettings

    def get_queryset(self):
        queryset = Wishes.objects.filter(user=self.request.user)
        return queryset
