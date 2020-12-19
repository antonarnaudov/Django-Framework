from django.shortcuts import render

from Photos.models.category_model import Category
from Photos.models.photos_model import Photos
from common_functionality.get_public_or_private_file import get_public_or_private_files


def work(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'pages/work.html', context)


def get_category_photos(request, category, fk):
    photos = Photos.objects.filter(category_id=fk)

    for photo in photos:
        if photo.wishes_set.filter(user_id=request.user.id).exists():
            photo.is_wished = True
        else:
            photo.is_wished = False

        if photo.shoppingcart_set.filter(user_id=request.user.id).exists():
            photo.is_added_to_cart = True
        else:
            photo.is_added_to_cart = False

    context = {
        'photos': photos,
        'category_name': category
    }
    return render(request, 'pages/photos.html', context)


def get_wishlist(request):
    context = {
        'wishlist': request.user.wishes_set.all(),
    }
    return render(request, 'user/wishlist.html', context)


def get_cart(request):
    cart = request.user.shoppingcart_set.all()
    cart.sum = 0
    for item in cart:
        cart.sum += item.photo.price

    context = {
        'cart': cart
    }
    return render(request, 'user/shopping_cart.html', context)


def get_public_file(request, path_to_file):
    return get_public_or_private_files(request, path_to_file, 'public')


def get_private_file(request, path_to_file):
    return get_public_or_private_files(request, path_to_file, 'private')
