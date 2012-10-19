from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import datetime
from jobs.models import Company, Job, JobFeed
from settings import *
from feedparsing import get_feed_articles
from jobs.forms import CompanyForm, JobForm

def index(request):
    job_list = Job.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')
    feed_job_list = get_feed_articles('job_feed_articles', JobFeed)
    return render_to_response('jobs/index.html', {
            'job_list': job_list,
            'feed_job_list': feed_job_list})

@login_required
@csrf_protect
def create(request):
    if request.POST:
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published = article.created
            article.save()
            return redirect(article)
    else:
        form = JobForm()

    return render_to_response('jobs/create.html', RequestContext(request, {
        'form': form
    }))


@login_required
@csrf_protect
def create_company(request):
    if request.POST:
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published = article.created
            article.save()
            return redirect(article)
    else:
        form = CompanyForm()

    return render_to_response('jobs/create-company.html', RequestContext(request, {
        'form': form
    }))
