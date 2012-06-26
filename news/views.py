from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from news.models import Article

def index(request):
    latest = Article.objects.all().order_by('-published')
    return render_to_response('news/index.html', {'latest': latest})

def view(request, id, slug):
    article = get_object_or_404(Article, pk=id)
    return render_to_response('news/view.html', RequestContext(request, {'article': article}))
