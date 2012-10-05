from django.core.management.base import BaseCommand, CommandError
import eatMedia.utils as utils

class Command(BaseCommand):
  args = '... (args) ...'
  help = 'Ingest media - spiders specified folder structures and pre-renders thumbnails'

  def handle(self, *args, **options):

    out = utils.ingest('/')

    for line in out:
      self.stdout.write(line + "\n")