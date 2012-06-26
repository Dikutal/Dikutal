from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from news.models import Article, NewsArticle

def article_index(request):
    latest = Article.objects.all().order_by('-published')
    return render_to_response('news/index.html', {'latest': latest})

def article_view(request, id, slug):
    article = get_object_or_404(Article, pk=id)
    return render_to_response('news/view.html', RequestContext(request, {'article': article}))

def news_index(request):
    latest = NewsArticle.objects.all().order_by('-published')
    return render_to_response('news/index.html', {'latest': latest})

def news_view(request, id, slug):
    article = get_object_or_404(NewsArticle, pk=id)
    return render_to_response('news/view.html', RequestContext(request, {'article': article}))
