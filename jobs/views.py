from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from jobs.models import Company, Job, JobFeed
from settings import *
from util.feedparsing import get_feed_articles
from jobs.forms import CompanyForm, JobForm

def index(request):
    articles = Job.objects.filter(published__lt=datetime.now(),
                                  deadline__gt=datetime.now()).order_by('-published')
    paginator = Paginator(articles, 10)

    page = request.GET.get('page')
    try:
        latest = paginator.page(page)
    except PageNotAnInteger:
        latest = paginator.page(1)
    except EmptyPage:
        latest = paginator.page(paginator.num_pages)

    feed_job_list = get_feed_articles('job_feed_articles', JobFeed)

    return render_to_response('jobs/index.html', {
            'job_list': latest,
            'feed_job_list': feed_job_list})

def view(model, request, id, slug):
    job = get_object_or_404(model, pk=id)
    return render_to_response('jobs/detail.html', RequestContext(request, {
        'job': job,
        'job_address': job.address or job.company.company_address,
        'show': job.is_shown(),
        'can_edit': job.can_edit(request.user),
    }))

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


def jobs_view(request, id, slug):
    return view(Job, request, id, slug)
