from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from news.forms import ArticleForm

from news.models import Article

import datetime

def index(model, request):
    articles = model.objects.filter(published__lt=datetime.datetime.now()).order_by('-published')
    paginator = Paginator(articles, 10)

    page = request.GET.get('page')
    try:
        latest = paginator.page(page)
    except PageNotAnInteger:
        latest = paginator.page(1)
    except EmptyPage:
        latest = paginator.page(paginator.num_pages)

    return render_to_response('news/index.html', {'latest': latest})

def view(model, request, id, slug):
    article = get_object_or_404(model, pk=id)
    return render_to_response('news/view.html', RequestContext(request, {'article': article}))

@login_required
@csrf_protect
def news_create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            redirect(article)
    else:
        form = ArticleForm()
        return render_to_response('news/create.html', RequestContext(request, {
            'form': form
        }))


def news_index(request):
    return index(Article, request)

def news_view(request, id, slug):
    return view(Article, request, id, slug)
