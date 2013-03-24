from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from planet.models import PlanetFeed
from settings import *


def index(request):
    return render_to_response('planet/index.html', RequestContext(request, {
            'articles': PlanetFeed.get_articles(),
            'active_tab':'planet',
            }))

def overview(request):
    return render_to_response('planet/overview.html', RequestContext(request, {
            'active_tab':'planet',
            'articles': PlanetFeed.get_articles(),
            }))
