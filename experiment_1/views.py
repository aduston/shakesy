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
    subs_json = json.dumps([
            { "start_time": cs.start_time,
             "text": cs.text } 
            for cs in models.ContemporarySubtitle.objects.all()])
    return render_to_response(
        "experiment_1.html",
        { "yt_query_string": yt_query_string,
          "subtitles": subs_json },
        context_instance=RequestContext(request))
