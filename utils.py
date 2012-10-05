from eatMedia.models import Folder, Item, ItemType
from django.conf import settings
import random
import string
from sorl.thumbnail import get_thumbnail
import os
import logging

def getItemType(name):
  try:
    item_type = ItemType.objects.get(name=name)
  except:
    item_type = ItemType(name=name)
    item_type.save()

  return item_type

def getUID(size=10, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def slugify(slug):
  slug = slug.replace(' ', '-')
  slug = slug.replace('(', '')
  slug = slug.replace(')', '')
  slug = slug.lower()
  return slug

def preRenderThumb(path):
  im = get_thumbnail(path, '100x100', crop='center', quality=99)
  print path


def ingest(path):

  # loop through media root(s) and create folder objects if they don't already exist
  # drop in a meta file containing folder id
  # check there isn't already a meta file in the folder root - if there is, the folder has been
  # renamed, so update the folder record

  out = []

  import imghdr

  for media_root in settings.EATMEDIA_ROOTS:
    items = os.listdir(media_root)
    for item in items:
      folder_path = os.path.join(media_root, item)


      if os.path.isdir(folder_path) and item != 'cache':

        folder = False

        # see if we have a folder with this path
        try:
          folder = Folder.objects.get(file_path=folder_path)
        except:

          # TODO: check for presence of meta file with old id

          # create new folder
          uid = getUID()
          folder = Folder(file_path=folder_path, name=item, slug=slugify(item), uid=uid)
          folder.save()

          out.append('created Folder ' + item)

          meta_file_path = os.path.join(folder_path, '._eatMedia.meta')
          meta_file = open(meta_file_path, 'w')
          meta_file.write('uid:' + uid)
          meta_file.close

        # loop through files in the folder
        folder_items = os.listdir(folder_path)
        for folder_item in folder_items:
          folder_item_path = os.path.join(folder_path, folder_item)
          if os.path.isfile(folder_item_path) and (not folder_item.startswith('.')):
            out.append('found file ' + folder_item)

            # get the file type
            try:
              file_type = imghdr.what(folder_item_path)
            except:
              file_type = 'unknown'

            if not file_type:
              file_type = 'unknown'

            out.append(file_type)
            
            # see if we already have a file with this filename in this folder
            try:
              media_item = Item.objects.get(folder=folder, name=folder_item)
            except:

              media_item = Item(folder=folder, name=folder_item, file_name=folder_item, item_type=getItemType(file_type))
              media_item.save()
              out.append('added ' + folder_item)
  return out
