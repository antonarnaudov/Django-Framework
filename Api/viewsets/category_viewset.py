from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from Api.serializers.category_serializer import CategorySerializer, PutCategorySerializer
from Photos.models.category_model import Category
from common_functionality.pagination_classes import CursorPaginationSettings


class CategoryViewSet(ModelViewSet):
    """
    ViewSet supporting all operations for Category.
    """
    queryset = Category.objects.all()

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('category',)
    ordering = 'category'
    pagination_class = CursorPaginationSettings

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return PutCategorySerializer

        return CategorySerializer
