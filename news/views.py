from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from news.forms import ArticleForm
from news.models import Article
from datetime import datetime

# Number of articles to show
NUM_ARTICLES = 15

def index(model, request):
    articles = model.objects.filter(published__lt=datetime.now()).order_by('-published')
    paginator = Paginator(articles, NUM_ARTICLES)

    page = request.GET.get('page')
    try:
        latest = paginator.page(page)
    except PageNotAnInteger:
        latest = paginator.page(1)
    except EmptyPage:
        latest = paginator.page(paginator.num_pages)

    return render_to_response('news/index.html', RequestContext(request, {
        'active_tab': 'articles',
        'subtitle': 'Articles',
        'latest': latest,
    }))

def view(model, request, id, slug):
    article = get_object_or_404(model, pk=id)
    return render_to_response('news/view.html', RequestContext(request, {
        'active_tab': 'articles',
        'subtitle': article.title,
        'article':  article,
        'can_edit': article.can_edit(request.user),
    }))

@login_required
@csrf_protect
def news_create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published = datetime.now()
            article.save()
            return redirect(article)
    else:
        form = ArticleForm()

    return render_to_response('news/create.html', RequestContext(request, {
        'active_tab': 'articles',
        'subtitle': 'Create article',
        'form': form,
    }))

@login_required
@csrf_protect
def news_edit(request, id):
    article = get_object_or_404(Article, pk=id)

    if not article.can_edit(request.user):
        return HttpResponseForbidden()

    if request.POST:
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)

    return render_to_response('news/edit.html', RequestContext(request, {
        'active_tab': 'articles',
        'subtitle': 'Edit article',
        'form': form,
    }))

def news_index(request):
    return index(Article, request)

def news_view(request, id, slug):
    return view(Article, request, id, slug)
