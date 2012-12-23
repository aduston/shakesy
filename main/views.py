from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
import urllib

def experiment_1(request):
    yt_query_string = urllib.urlencode(
        { "enablejsapi": "1",
          "origin": settings.ORIGIN })
    return render_to_response(
        "experiment_1.html",
        { "yt_query_string": yt_query_string },
        context_instance=RequestContext(request))
