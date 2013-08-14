from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from news.models import Article
from planet.models import PlanetFeed
from jobs.models import Job
from operator import itemgetter
from django.core.cache import cache
from planet.models import PlanetFeed
from util.languages import *
import datetime
import feedparser
from settings import *


# Number of Q&A questions to show on the front page
NUM_QA_INDEX = 5

# Number of jobs to show on the front page
NUM_JOBS_INDEX = 5

# Number of blog articles to show on the front page
NUM_BLOG_ARTICLES_INDEX = 5

# Number of articles to show on the front page
NUM_ARTICLES_INDEX = 15


def get_qa_entries():
    qa_feed = cache.get('qa_cache')
    if not qa_feed:
        qa_feed = feedparser.parse('http://qa.dikutal.dk/questions/?type=rss')
        cache.set('qa_cache',qa_feed,FEED_CACHE_DURATION)
    items = qa_feed.entries[:NUM_QA_INDEX]
    for i in items:
        d = i['published']
        i['date'] = d[5:7] + '.' + d[7:16]
    return items

def get_latest_jobs(lang):
    jobs = Job.objects.filter(published__lt=datetime.datetime.now())
    jobs = filter_with_lang(jobs, lang)
    jobs = jobs.order_by('-published')[:NUM_JOBS_INDEX]
    return jobs

def get_blog_articles():
    articles = PlanetFeed.get_articles()[:NUM_BLOG_ARTICLES_INDEX]
    return articles

def get_articles(lang):
    articles = Article.objects.filter(published__lt=datetime.datetime.now())
    articles = filter_with_lang(articles, lang)
    articles = articles.order_by('-published')
    content = [(a, datetime.datetime.now() - a.published) for a in articles]
    return [{'content': c} for (c, v) in sorted(content, key=itemgetter(1))][:NUM_ARTICLES_INDEX]

def index(request):
    lang = request.GET.get('lang')
    if not lang in lang_filter.keys():
        lang = 'all'
    return render_to_response('frontpage/index.html', RequestContext(request, {
        'qa_items': get_qa_entries(),
        'latest_jobs': get_latest_jobs(lang),
        'latest_blog_articles': get_blog_articles(),
        'feed_items': get_articles(lang),
        'subtitle': 'Home',
        'active_lang': lang
    }))
