from django.shortcuts import render_to_response, get_object_or_404, redirect
from news.models import Article
from jobs.models import Job

import datetime

NUM_LATEST=5

def index(request):
    articles = Article.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')[:NUM_LATEST]
    jobs = Job.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')[:NUM_LATEST]

    return render_to_response('frontpage/index.html', {
        'latest_articles': articles,
        'latest_jobs':     jobs,
    })
