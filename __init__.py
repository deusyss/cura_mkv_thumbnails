# Copyright (c) 2023 cura_mkv_thumbnails
# The cura_mkv_thunbnails plugin is released under the terms of the AGPLv3 or higher.

from . import cura_mkv_thumbnails


def getMetaData():
    return {}


def register(app):
    return {"extension": cura_mkv_thumbnails.MkvThumbnailsSnapshot()}
