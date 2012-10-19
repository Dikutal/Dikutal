from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from jobs.models import Job, JobFeed
from settings import *
from feedparsing import get_feed_articles

def index(request):
    job_list = Job.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')
    feed_job_list = get_feed_articles('job_feed_articles', JobFeed)
    return render_to_response('jobs/index.html', {
            'job_list': job_list,
            'feed_job_list': feed_job_list})
