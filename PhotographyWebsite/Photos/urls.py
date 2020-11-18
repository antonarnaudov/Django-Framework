from django.urls import path

from Photos.views.photos_view import add_photo, edit_photo, delete_photo
from Photos.views.views import work, get_public_file, get_private_file

urlpatterns = [
    path('', work, name='work page'),
    path('resources_public/<path:path_to_file>/', get_public_file, name='public file'),
    path('resources_private/<path:path_to_file>/', get_private_file, name='private file'),

    path('photo/add/', add_photo, name='add-photo'),
    path('photo/edit/<int:pk>/', edit_photo, name='edit-photo'),
    path('photo/delete/<int:pk>/', delete_photo, name='delete-photo')

]
