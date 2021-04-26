from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from Api.serializers.shopping_cart_serializer import ShoppingCartSerializer
from Photos.models.shopping_cart import ShoppingCart
from common_functionality.pagination_classes import CursorPaginationSettings


# NOTE: ordering_fields does NOT support nested fields


class ShoppingCartListApiView(ListAPIView):
    serializer_class = ShoppingCartSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('photo__name',)
    ordering_fields = ''
    ordering = 'photo_id'
    pagination_class = CursorPaginationSettings

    def get_queryset(self):
        queryset = ShoppingCart.objects.filter(user=self.request.user)
        return queryset
