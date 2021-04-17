from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
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

class CategoryPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 100


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('id', )
    search_fields = ('category',)
    pagination_class = CategoryPagination
