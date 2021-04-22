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

# TODO: Fix Ordering Fields


class WishesListApiView(ListAPIView):
    # queryset = Wishes.objects.all()
    serializer_class = WishesSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = ('price', )
    search_fields = ('photo__name',)
    # ordering_fields = ['photo__price']  # photos because of the model name
    ordering = 'photo_id'
    pagination_class = CursorPaginationSettings

    def get_queryset(self):
        queryset = Wishes.objects.filter(user=self.request.user)
        return queryset
