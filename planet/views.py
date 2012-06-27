import time
import datetime
import itertools
import feedparser
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from planet.models import Feed
import dikutaltimezone as dtz
     
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
        try:
             parsed = entry.updated_parsed
        except AttributeError:
             parsed = entry.published_parsed
        self.updated = datetime.datetime.fromtimestamp(
            time.mktime(parsed), dtz.utc)
        self.updated += dtz.copenhagen.utcoffset(self.updated)
        self.updated = self.updated.astimezone(dtz.copenhagen)
        self.updated_formatted = self.updated.strftime('%A, %d %B %Y %H:%M:%S %z')

def index(request):
    feeds = Feed.objects.all()
    feeds = (map(FeedArticle, feedparser.parse(feed.url).entries)
             for feed in feeds)
    articles = list(itertools.chain(*feeds))
    articles.sort(key=lambda article: article.updated, reverse=True)

    return render_to_response('planet/index.html', {'articles': articles})
