from django.core.management.base import BaseCommand
from django.conf import settings
from experiment_1 import models
import re
import os

CHARACTERS = {'1': models.Character(name="Barnardo", title="Barnardo", description="Barnardo"),
              '2': models.Character(name="Francisco", title="Franciso", description="Francisco"),
              '3': models.Character(name="Horatio", title="Horatio", description="Horatio"),
              '4': models.Character(name="Marcellus", title="Marcellus", description="Marcellus")}

OUT_OF_SUBTITLE = 0
SUBTITLE_NUMBER = 1
SUBTITLE_TIME = 2
SUBTITLE_FIRST_LINE = 3
SUBTITLE_LINE = 4

[c.save() for c in CHARACTERS.values()]
CHARACTERS['0'] = None


class Command(BaseCommand):
    def handle(self, *args, **options):
        original_subs = self._parse("original_text.srt")
        contemporary_subs = self._parse("contemporary_text.srt")

        i = 0
        for orig_sub, contemp_sub in zip(original_subs, contemporary_subs):
            print "Subtitle %d" % i
            models.Subtitle(contemporary_text=contemp_sub['Line'],
                    original_text=orig_sub['Line'], character=orig_sub['Character'], start_time=orig_sub['Time']).save()
            i += 1

    def _parse(self, file_name):
        file_name = os.path.join(settings.DATA_DIR, file_name)
        with open(file_name, "r") as f:
            return self._parse_text(f.read())

    def _parse_time(self, line):
        time = 0
        time_line = line.split(' --> ')[0]

        h, m, s = time_line.split(":")
        s, millisec = s.split(',')

        time += (int(h) * 36000) + (int(m) * 600) + (int(s) * 10)
        time += int(millisec) / 100.0
        return time

    def _parse_text(self, text):
        state = OUT_OF_SUBTITLE
        subs = []
        sub = dict()
        sub['Line'] = ''
        for line in text.splitlines():
            if state == OUT_OF_SUBTITLE and line != '':
                state = SUBTITLE_TIME
            elif state == SUBTITLE_TIME:
                sub['Time'] = self._parse_time(line)
                state = SUBTITLE_FIRST_LINE
            elif state == SUBTITLE_FIRST_LINE:
                line2 = line.split(":")
                sub['Character'] = CHARACTERS[line2[0]]
                sub['Line'] += line2[1]
                state = SUBTITLE_LINE
            elif state == SUBTITLE_LINE:
                if line != '':
                    sub['Line'] += '\n' + line
                else:
                    subs.append(sub)
                    sub = dict()
                    sub['Line'] = ''
                    state = OUT_OF_SUBTITLE
        if state != OUT_OF_SUBTITLE: # We still have a subtitle
            subs.append(sub)
        return subs
