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
        original_subs = self._parse("original_text.srt")
        contemporary_subs = self._parse("contemporary_text.srt")

        i = 0
        for sub in original_subs:
            start = sub.start.hours * 36000 + sub.start.minutes * 600 + sub.start.seconds * 10 + sub.start.milliseconds / 100.0
            print "Subtitle %d" % sub.index
            models.Subtitle(contemporary_text=contemporary[i].text[2:], original_text=sub.text[2:], character=CHARACTERS[sub.text[0]], start_time=start).save()
            i += 1

    def _parse(self, file_name):
        file_name = os.path.join(settings.DATA_DIR, file_name)        
        with open(file_name, "r") as f:
            return self._parse_text(f.read())

    def _parse_text(self, text):
        pattern = re.compile(self._pattern(), re.DOTALL)
        match = pattern.search(text)
        

    def _pattern(self):
        pattern = r'\d+\s*?\n'
        pattern += r'(?P<s_hour>\d{2}):(?P<s_min>\d{2}):(?P<s_sec>\d{2})(,(?P<s_secfr>\d*))?'
        pattern += r' --> '
        pattern += r'(?P<e_hour>\d{2}):(?P<e_min>\d{2}):(?P<e_sec>\d{2})(,(?P<e_secfr>\d*))?'
        pattern += r'\n(\n|(?P<text>.+?)\n\n)'
        return pattern
