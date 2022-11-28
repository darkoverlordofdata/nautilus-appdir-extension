"""
Support AppDir style folders: utils

darkoverlordofdata
"""
import os

def get_icon(path, name):

    with_png = path.replace('.app', f'.app/Resources/{name}.png')
    if os.path.isfile(with_png):
        return with_png

    with_jpg = path.replace('.app', f'.app/Resources/{name}.jpg')
    if os.path.isfile(with_jpg):
        return with_jpg

    with_jpeg = path.replace('.app', f'.app/Resources/{name}.jpeg')
    if os.path.isfile(with_jpeg):
        return with_jpeg

    with_tiff = path.replace('.app', f'.app/Resources/{name}.tiff')
    if os.path.isfile(with_tiff):
        return with_tiff

    return path.replace('.app', f'.app/Resources/{name}.???')
