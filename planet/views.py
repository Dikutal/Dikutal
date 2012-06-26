import time
import datetime
import itertools
import feedparser
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from planet.models import Feed

class GMT1(datetime.tzinfo):
     def utcoffset(self, dt):
         return timedelta(hours=1)

     def dst(self, dt):
         return timedelta(0)

     def tzname(self,dt):
         return "Europe/Copenhagen"

class FeedArticle(object):
    def __init__(self, entry):
        '''
        Creates a FeedArticle object from a feedparser entry
        '''
        self.title = entry.title
        self.url = entry.links[0]['href']
        try:
            self.html = entry.content[0].value
        except AttributeError:
            self.html = '<p>' + entry.summary + '</p>'
        self.updated = datetime.datetime.fromtimestamp(
            time.mktime(entry.updated_parsed)).astimezone(GMT1)
        self.updated_formatted = self.updated.isoformat()

def index(request):
    feeds = Feed.objects.all()
    articles = list(itertools.chain(
            *(map(FeedArticle, feedparser.parse(feed.url).entries)
              for feed in feeds)))
    articles.sort(key=lambda article: article.updated, reverse=True)

    return render_to_response('planet/index.html', {'articles': articles})
