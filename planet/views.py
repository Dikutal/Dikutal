from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from planet.models import Feed
import itertools
import feedparser

def index(request):
    feeds = Feed.objects.all()
    articles = list(itertools.chain(*(feedparser.parse(feed.url).entries for feed in feeds)))
    return render_to_response('planet/index.html', {'articles': articles})
