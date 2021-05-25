from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from Api.serializers.shopping_cart_serializer import AddToShoppingCartSerializer, ShowShoppingCartSerializer, \
    ShowBoughtItemsSerializer
from Photos.models.shopping_cart import ShoppingCart
from common_functionality.mixins import SerializerRequestSwitchMixin


# NOTE: ordering_fields does NOT support nested fields

class ShoppingCartViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    """
    ViewSet supporting all operations for ShoppingCart.
    """
    serializers = {
        'show': ShowShoppingCartSerializer,
        'create': AddToShoppingCartSerializer,
        'update': AddToShoppingCartSerializer,
        'detailed': AddToShoppingCartSerializer,

    }

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('photo__name',)
    ordering_fields = ''
    ordering = 'photo_id'

    def get_queryset(self):
        queryset = ShoppingCart.objects.filter(user=self.request.user)
        return queryset


class BoughtItemsListAPIView(ListAPIView):
    """
    APIListView returns all information for paid photos.
    """
    serializer_class = ShowBoughtItemsSerializer
    pagination_class = None

    def get_queryset(self):
        """
        Filtering for the current User
        """
        queryset = ShoppingCart.objects.filter(user=self.request.user)
        return queryset
