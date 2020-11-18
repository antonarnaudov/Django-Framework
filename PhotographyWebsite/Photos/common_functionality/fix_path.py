import os
import urllib.parse


def fix_path(path):
    path = urllib.parse.unquote(path)

    return path.replace('/', os.path.sep)
