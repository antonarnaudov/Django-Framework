from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Api.serializers.category_serializer import CategorySerializer
from Photos.models.category_model import Category


# class CategoryListApiView(APIView):
#     @staticmethod
#     def get(request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)


# get current page number from offset + 1
from common_functionality.pagination_classes import CursorPaginationSettings


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = ('id', )
    search_fields = ('category',)
    ordering = 'category'
    pagination_class = CursorPaginationSettings
