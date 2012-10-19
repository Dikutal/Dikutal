from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from planet.models import PlanetFeed
from settings import *
from util.feedparsing import get_feed_articles

def index(request):
    return render_to_response('planet/index.html', {
            'articles': get_feed_articles('planet_articles', PlanetFeed)})

def overview(request):
    return render_to_response('planet/overview.html', {
            'articles': get_feed_articles('planet_articles', PlanetFeed)})
