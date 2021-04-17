from django.urls import path

from Api.viewsets.category_viewset import CategoryListApiView
from Api.viewsets.photos_viewset import PhotosListApiView
from Api.viewsets.user_viewset import UserListApiView

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='work page api'),
    path('photos/', PhotosListApiView.as_view(), name='photos page api'),
    path('user/', UserListApiView.as_view(), name='user data api')
]
