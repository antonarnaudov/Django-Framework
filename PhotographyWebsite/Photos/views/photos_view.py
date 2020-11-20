from django.shortcuts import render, redirect

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
        # TODO: Implement the watermarked_photo creation logic.

        form = PhotosForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
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
    photo.delete()
    return redirect('work page')
