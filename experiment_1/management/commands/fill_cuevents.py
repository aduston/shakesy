from django.core.management.base import BaseCommand
from django.conf import settings
from pysrt import SubRipFile
from experiment_1 import models
import os

CHARACTERS = {'1': models.Character(name="Barnardo", title="Barnardo", description="Barnardo"),
              '2': models.Character(name="Francisco", title="Franciso", description="Francisco"),
              '3': models.Character(name="Horatio", title="Horatio", description="Horatio"),
              '4': models.Character(name="Marcellus", title="Marcellus", description="Marcellus")}


[c.save() for c in CHARACTERS.values()]
CHARACTERS['0'] = None

class Command(BaseCommand):
    def handle(self, *args, **options):
        for data_file in os.listdir(settings.DATA_DIR):
            subs = SubRipFile.open(os.path.join(settings.DATA_DIR, data_file))
            for sub in subs:
                start = sub.start.hours * 6000 + sub.start.minutes * 600 + sub.start.seconds * 10 + sub.start.milliseconds / 10.0
                print "Subtitle %d" % sub.index
                models.ContemporarySubtitle(text=sub.text[2:], character=CHARACTERS[sub.text[0]], start_time=start).save()
