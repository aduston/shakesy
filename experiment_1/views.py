from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
import models
import json
import urllib

def index(request):
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
        "experiment_1.html",
        { "yt_query_string": yt_query_string,
          "characters": models.Character.objects.all(),
          "subtitles": json.dumps(subs_dicts) },
        context_instance=RequestContext(request))
