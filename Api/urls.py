from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Api.viewsets.category_viewset import CategoryViewSet
from Api.viewsets.photos_viewset import PhotosViewSet
from Api.viewsets.shopping_cart_viewset import ShoppingCartViewSet, BoughtItemsListAPIView
from Api.viewsets.user_viewset import UserListApiView
from Api.viewsets.wishes_viewset import WishesViewSet

router = DefaultRouter()
router.register(r'photos', PhotosViewSet, basename='photos')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'wishes', WishesViewSet, basename='wishes')
router.register(r'cart', ShoppingCartViewSet, basename='cart')

urlpatterns = [
    path('router/', include(router.urls)),

    path('bought/', BoughtItemsListAPIView.as_view(), name='bought'),
    path('user/', UserListApiView.as_view(), name='user data api'),
]
