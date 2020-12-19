from django.urls import path

from Photos.views.category_view import add_category, edit_category, delete_category
from Photos.views.photos_view import add_photo, edit_photo, delete_photo, wish_photo, add_to_cart
from Photos.views.views import work, get_public_file, get_private_file, get_category_photos, get_wishlist, get_cart

urlpatterns = [
    # Home page:
    path('', work, name='work page'),
    path('<str:category>/<int:fk>/photos', get_category_photos, name='category photos'),
    path('resources_public/<path:path_to_file>/', get_public_file, name='public file'),
    path('resources_private/<path:path_to_file>/', get_private_file, name='private file'),

    # Category operations pages:
    path('category/add/', add_category, name='add-category'),
    path('category/edit/<int:pk>/', edit_category, name='edit-category'),
    path('category/delete/<int:pk>/', delete_category, name='delete-category'),

    # Photo operations pages:
    path('photo/add/', add_photo, name='add-photo'),
    path('photo/edit/<int:pk>/', edit_photo, name='edit-photo'),
    path('photo/delete/<int:pk>/', delete_photo, name='delete-photo'),

    # Wishes:
    path('wish/<int:pk>/', wish_photo, name='wish'),
    path('wishlist/', get_wishlist, name='wishlist page'),

    # ShoppingCart:
    path('add_to_cart/<int:pk>/', add_to_cart, name='add to cart'),
    path('cart/', get_cart, name='cart page')
]
