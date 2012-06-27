from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from news.models import Article, NewsArticle

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

def article_index(request):
    return index(Article, request)

def news_index(request):
    return index(NewsArticle, request)

def article_view(request, id, slug):
    return view(Article, request, id, slug)

def news_view(request, id, slug):
    return view(NewsArticle, request, id, slug)
