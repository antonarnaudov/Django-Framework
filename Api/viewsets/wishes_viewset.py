from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from Api.serializers.wishes_serializer import CreateWishesSerializer, ShowWishesSerializer
from Photos.models.wishes_model import Wishes
from common_functionality.mixins import SerializerRequestSwitchMixin


# NOTE: ordering_fields does NOT support nested fields

class WishesViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    """
    ViewSet supporting all operations for Wishes.
    """
    serializers = {
        'show': ShowWishesSerializer,
        'create': CreateWishesSerializer,
        'update': CreateWishesSerializer
    }

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('photo__name',)
    ordering_fields = ''
    ordering = 'photo_id'

    def get_queryset(self):
        """
        Filtering for the current User
        """
        queryset = Wishes.objects.filter(user=self.request.user)
        return queryset
