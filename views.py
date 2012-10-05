from django.template import Context, loader
from eatMedia.models import Folder, Item, ItemType
import eatMedia.utils as utils
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

  out = utils.ingest('/')

  return HttpResponse(out)



  # loop through folders and delete folder records where the path no londer exists

