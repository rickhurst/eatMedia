from django.template import Context, loader
from eatMedia.models import Folder, Item, ItemType
from eatMedia.utils import getItemType
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404

import os
import logging

def home(request):
  folders = Folder.objects.all()

  t = loader.get_template('home.html')
  c = Context({'folders': folders,})

  return HttpResponse(t.render(c))

def folder(request, slug):
  f = get_object_or_404(Folder, slug=slug)
  return render_to_response('folder.html', {'folder': f })

def ingest(request):

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
          folder = Folder(file_path=folder_path, name=item, slug=item)
          folder.save()

          out.append('created Folder ' + item)

          meta_file_path = os.path.join(folder_path, '._id.meta')
          meta_file = open(meta_file_path, 'w')
          meta_file.write(str(folder.id))
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

            out.append(file_type)
            
            # see if we already have a file with this filename in this folder
            try:
              media_item = Item.objects.get(folder=folder, name=folder_item)
            except:

              media_item = Item(folder=folder, name=folder_item, file_name=folder_item, item_type=getItemType(file_type))
              media_item.save()
              out.append('added ' + folder_item)





  return HttpResponse(out)



  # loop through folders and delete folder records where the path no londer exists

