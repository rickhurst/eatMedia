from eatMedia.models import ItemType
import random
import string
from sorl.thumbnail import get_thumbnail

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
