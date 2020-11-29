from django.shortcuts import render, redirect

from Photos.common_functionality.path_functions import clean_files_from_path
from Photos.forms.category_form import CategoryForm
from Photos.models.category_model import Category


def add_or_edit_category(request, category, template_name):
    if request.method == 'GET':
        context = {
            'form': CategoryForm(instance=category),
            'category': category,
        }
        return render(request, template_name, context)
    else:
        old_image = category.image

        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            if old_image:
                if old_image != form.cleaned_data['image']:
                    clean_files_from_path(old_image.path)
            form.save()
            return redirect('work page')
        context = {
            'form': form,
            'category': category,
        }
        return render(request, template_name, context)


def add_category(request):
    return add_or_edit_category(request, Category(), 'creator/add_category.html')


def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    return add_or_edit_category(request, category, 'creator/edit_category.html')


def delete_category(request, pk):
    category = Category.objects.get(pk=pk)

    clean_files_from_path(category.image.path)
    category.delete()
    return redirect('work page')
