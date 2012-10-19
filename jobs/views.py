from django.http import HttpResponse
from django.shortcuts import render_to_response
from jobs.models import JobFeed
from settings import *
from feedparsing import get_feed_articles

def index(request):
    return render_to_response('jobs/index.html', {
            'feed_jobs': get_feed_articles(request, 'job_feed_articles', JobFeed)})
