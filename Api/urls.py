from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Api import views
from Api.viewsets.category_viewset import CategoryListApiView
from Api.viewsets.photos_viewset import PhotosListApiView, PhotosViewSet
from Api.viewsets.shopping_cart_viewset import ShoppingCartListApiView
from Api.viewsets.user_viewset import UserListApiView
from Api.viewsets.wishes_viewset import WishesListApiView

router = DefaultRouter()
router.register(r'photos', PhotosViewSet, basename='photos')

urlpatterns = [
    path('router/', include(router.urls)),

    path('categories/', CategoryListApiView.as_view(), name='work page api'),
    path('wishes/', WishesListApiView.as_view(), name='wishes page api'),
    path('user/', UserListApiView.as_view(), name='user data api'),
    path('cart/', ShoppingCartListApiView.as_view(), name='card page api'),
]
