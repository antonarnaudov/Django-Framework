from os.path import join, isfile

from django.conf import settings
from django.http import HttpResponse

from Photos.common_functionality.path_functions import fix_path


# TODO: Implement the access logic once the profiles are done.
def has_access():
    return True


def get_public_or_private_files(request, path_to_file, file_type: str):
    full_path = fix_path(join(settings.MEDIA_ROOT, file_type, path_to_file[len(f'/media/{file_type}/'):]))

    if isfile(full_path):
        if has_access():
            file = open(full_path, 'rb')
            response = HttpResponse(content=file)
            response['Content-Disposition'] = 'attachment'
            return response
    return None
