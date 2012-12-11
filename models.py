from django.db import models
import os

class Folder(models.Model):
  file_path = models.CharField(max_length=500)
  name = models.CharField(max_length=200)
  slug = models.CharField(max_length=200)
  uid = models.CharField(max_length=30, blank=True)

  def __unicode__(self):
    return self.name

  def images(self):
    images = Item.objects.filter(folder=self, item_type=1)
    return images

# class Set(models.Model):
#   name = models.CharField(max_length=200)

class ItemCategory(models.Model):
  name = models.CharField(max_length= 200)

  def __unicode__(self):
    return self.name 


class ItemType(models.Model):
  name = models.CharField(max_length=200)
  category = models.ForeignKey(ItemCategory, null=True)

  def __unicode__(self):
    return self.name


class Item(models.Model):
  file_name = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  folder = models.ForeignKey(Folder)
  item_type = models.ForeignKey(ItemType)

  def getFilePath(self):
    path = os.path.join(self.folder.file_path, self.file_name)
    return path
    

  def __unicode__(self):
    return self.name

