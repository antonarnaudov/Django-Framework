from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Api.viewsets.category_viewset import CategoryViewSet
from Api.viewsets.photos_viewset import PhotosViewSet
from Api.viewsets.shopping_cart_viewset import ShoppingCartListApiView
from Api.viewsets.user_viewset import UserListApiView
from Api.viewsets.wishes_viewset import WishesViewSet

router = DefaultRouter()
router.register(r'photos', PhotosViewSet, basename='photos')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'wishes', WishesViewSet, basename='wishes')

urlpatterns = [
    path('router/', include(router.urls)),

    path('user/', UserListApiView.as_view(), name='user data api'),
    path('cart/', ShoppingCartListApiView.as_view(), name='card page api'),
]
