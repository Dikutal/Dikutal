import feedparser
from django.core.cache import cache
from settings import *
import dikutaltimezone as dtz
import time
import datetime
import itertools

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

def get_feed_articles(cache_name, feed_obj):
    articles = cache.get(cache_name)
    if articles is None:
        feeds = feed_obj.objects.all()
        feeds = (map(FeedArticle, feedparser.parse(feed.url).entries)
                 for feed in feeds)
        articles = list(itertools.chain(*feeds))
        articles.sort(key=lambda article: article.updated, reverse=True)
        cache.set(cache_name, articles, FEED_CACHE_DURATION)
    return articles
