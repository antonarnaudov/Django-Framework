from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Api.serializers.category_serializer import ShowCategorySerializer, UpdateCategorySerializer
from Photos.models.category_model import Category
from common_functionality.mixins import SerializerRequestSwitchMixin


# @parser_classes((FormParser,))
class CategoryViewSet(SerializerRequestSwitchMixin, ModelViewSet):
    """
    ViewSet supporting all operations for Category.
    """
    queryset = Category.objects.all()
    serializers = {
        'show': ShowCategorySerializer,
        'update': UpdateCategorySerializer
    }

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('category',)
    ordering = 'category'
