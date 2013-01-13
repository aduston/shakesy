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
              "character_id": cs.character.id,
              "text": cs.text } 
            for cs in models.ContemporarySubtitle.objects.all()]
    cur_character_ids = set([s["character_id"] for s in subs_dicts])
    
    return render_to_response(
        "experiment_1.html",
        { "yt_query_string": yt_query_string,
          "cur_characters": models.Character.objects.filter(id__in=cur_character_ids).all(),
          "other_characters": models.Character.objects.exclude(id__in=cur_character_ids).all(),
          "subtitles": json.dumps(subs_dicts) },
        context_instance=RequestContext(request))
