from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from Photos.forms.photos_form import PhotosForm
from Photos.models.photos_model import Photos
from Photos.models.wishes_model import Wishes
from Photos.views.views import get_category_photos
from common_functionality.path_functions import clean_files_from_path


def add_or_edit_photo(request, photo, template_name):
    if request.method == 'GET':
        context = {
            'form': PhotosForm(instance=photo),
            'photo': photo,
        }
        return render(request, template_name, context)
    else:
        (old_image, old_watermarked_image) = (photo.original_photo, photo.watermarked_photo)

        form = PhotosForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
            if old_image:
                if old_image != form.cleaned_data['original_photo']:
                    clean_files_from_path(old_image.path, old_watermarked_image.path)
            form.save()
            return redirect('work page')

        context = {
            'form': form,
            'photo': photo,
        }
        return render(request, template_name, context)


def add_photo(request):
    return add_or_edit_photo(request, Photos(), 'creator/add_photo.html')


def edit_photo(request, pk):
    photo = Photos.objects.get(pk=pk)
    return add_or_edit_photo(request, photo, 'creator/edit_photo.html')


def delete_photo(request, pk):
    photo = Photos.objects.get(pk=pk)

    clean_files_from_path(photo.original_photo.path, photo.watermarked_photo.path)
    photo.delete()
    return redirect('work page')


@login_required
def wish_photo(request, pk):
    wish = Wishes.objects.filter(user_id=request.user.id, photo_id=pk).first()
    photo = Photos.objects.get(pk=pk)

    if wish:
        wish.delete()
        photo.is_wished = False
    else:
        wish = Wishes(user=request.user)
        wish.photo = photo
        photo.is_wished = True
        wish.save()

    return get_category_photos(request, photo.category.category, photo.category.id)

    # photo = {
    #     'id': photo.id,
    #     'watermarked_photo': photo.watermarked_photo.url,
    #     'category': photo.category.category,
    #     'name': photo.name,
    #     'price': photo.price,
    #     'is_wished': photo.is_wished
    # }

    # data = {
    #     'photo': photo
    # }
    # return JsonResponse(data)
