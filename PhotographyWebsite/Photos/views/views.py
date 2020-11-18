from django.shortcuts import render

# Create your views here.
from Photos.common_functionality.get_public_or_private_file import get_public_or_private_files
from Photos.models import Photos


def work(request):
    context = {
        'photos': Photos.objects.all(),
    }
    return render(request, 'pages/work.html', context)


def get_public_file(request, path_to_file):
    return get_public_or_private_files(request, path_to_file, 'public')


def get_private_file(request, path_to_file):
    return get_public_or_private_files(request, path_to_file, 'private')
