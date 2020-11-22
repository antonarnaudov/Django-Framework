from django.shortcuts import render, redirect

from Photos.common_functionality.path_functions import clean_files_from_path
from Photos.forms.photos_form import PhotosForm
from Photos.models import Photos


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
