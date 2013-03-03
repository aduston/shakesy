from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
import models
import json
import urllib

def index_a(request):
    yt_query_string = urllib.urlencode(
        { "enablejsapi": "1",
          "origin": settings.ORIGIN })
    subs_dicts = [
            { "start_time": cs.start_time,
              "character_id": cs.character_id,
              "contemporary_text": cs.contemporary_text,
              "original_text": cs.original_text }
            for cs in models.Subtitle.objects.all().order_by("start_time")]

    return render_to_response(
        "experiment_1a.html",
        { "yt_query_string": yt_query_string,
          "characters": models.Character.objects.all(),
          "subtitles": json.dumps(subs_dicts) },
        context_instance=RequestContext(request))

def index_b(request):
    yt_query_string = urllib.urlencode(
        { "enablejsapi": "1",
          "origin": settings.ORIGIN })
    subs_dicts = [
            { "start_time": cs.start_time,
              "character_id": cs.character_id,
              "contemporary_text": cs.contemporary_text,
              "original_text": cs.original_text }
            for cs in models.Subtitle.objects.all().order_by("start_time")]

    char_dicts = dict([
            [c.id,
             { "id": c.id,
               "name": c.name,
               "title": c.title, 
               "image": c.cimage.url if c.cimage else "" }]
            for c in models.Character.objects.all()])

    return render_to_response(
        "experiment_1b.html",
        { "yt_query_string": yt_query_string,
          "characters": json.dumps(char_dicts),
          "subtitles": json.dumps(subs_dicts) },
        context_instance=RequestContext(request))
