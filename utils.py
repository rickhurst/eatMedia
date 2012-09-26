from eatMedia.models import ItemType

def getItemType(name):
  try:
    item_type = ItemType.objects.get(name=name)
  except:
    item_type = ItemType(name=name)
    item_type.save()

  return item_type