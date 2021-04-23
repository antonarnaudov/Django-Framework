import django_filters
from django_filters.rest_framework import FilterSet

from Photos.models.photos_model import Photos


class PhotosFilter(FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Photos
        fields = ['min_price', 'max_price']
