from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from news.models import Article
from planet.models import PlanetFeed
from jobs.models import Job
from operator import itemgetter

import datetime

NUM_LATEST=5
NUM_FEED=10

def index(request):
    feed = generate_feed()
    jobs = Job.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')[:NUM_LATEST]

    return render_to_response('frontpage/index.html', RequestContext(request, {
        'feed_items':  feed,
        'latest_jobs': jobs,
    }))

def generate_feed():
    articles = Article.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')[:NUM_FEED]
    blogs = PlanetFeed.get_articles()[:NUM_FEED]

    content = []
    content.extend((a, datetime.datetime.now() - a.published, "article") for a in articles)
    content.extend((b, 2*(datetime.datetime.utcnow() - b.updated.replace(tzinfo=None)), "blogpost") for b in blogs)

    return [{ 'content': c, 'type': t } for (c, v, t) in sorted(content, key=itemgetter(1))][:NUM_FEED]
