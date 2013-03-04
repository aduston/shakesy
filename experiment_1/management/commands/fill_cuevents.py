from django.core.management.base import BaseCommand
from django.conf import settings
from experiment_1 import models
import re
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
        for orig_sub, contemp_sub in zip(original_subs, contemporary_subs):
            print orig_sub
            start = int(orig_sub[0]) * 36000 + int(orig_sub[1]) * 600 + int(orig_sub[2]) * 10 + int(orig_sub[3]) / 100.0
            print "Subtitle %d" % i
            models.Subtitle(contemporary_text=contemp_sub[9], original_text=orig_sub[9], character=CHARACTERS[orig_sub[8]], start_time=start).save()
            i += 1

    def _parse(self, file_name):
        file_name = os.path.join(settings.DATA_DIR, file_name)
        with open(file_name, "r") as f:
            return self._parse_text(f.read())

    def _parse_text(self, text):
        pattern = re.compile(self._pattern(), re.DOTALL)
        match = pattern.findall(text)
        return match


    def _pattern(self):
        pattern = r'\d+\s*?\r?\n'
        pattern += r'(?P<s_hour>\d{2}):(?P<s_min>\d{2}):(?P<s_sec>\d{2}),(?P<s_secfr>\d*)'
        pattern += r' --> '
        pattern += r'(?P<e_hour>\d{2}):(?P<e_min>\d{2}):(?P<e_sec>\d{2}),(?P<e_secfr>\d*)\r?'
        pattern += r'\n(\d+):(?P<text>.+?)\r?\n'
        return pattern
