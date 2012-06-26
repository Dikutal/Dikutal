import itertools
import feedparser
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from planet.models import Feed

class FeedArticle(object):
    def __init__(self, entry):
        '''
        Creates a FeedArticle object from a feedparser entry
        '''
        self.title = entry.title
        try:
            self.html = entry.content[0].value
        except AttributeError:
            self.html = '<p>' + entry.summary + '</p>'
        self.updated = entry.updated_parsed

def index(request):
    feeds = Feed.objects.all()
    articles = list(itertools.chain(
            *(map(FeedArticle, feedparser.parse(feed.url).entries)
              for feed in feeds)))
    articles.sort(key=lambda article: article.updated, reverse=True)

    return render_to_response('planet/index.html', {'articles': articles})
