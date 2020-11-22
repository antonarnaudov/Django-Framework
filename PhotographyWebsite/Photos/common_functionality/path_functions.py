import os
import urllib.parse


def fix_path(path):
    path = urllib.parse.unquote(path)

    return path.replace('/', os.path.sep)


def clean_files_from_path(*args):
    for file in args:
        os.remove(file)
