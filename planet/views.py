from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from planet.models import PlanetFeed
from settings import *
from util.feedparsing import get_feed_articles
from planet.forms import PlanetForm
from django.utils.text import Truncator

def shorten_html(h, length):
    return Truncator(h).words(length, html=True)

def index(request):
    articles = PlanetFeed.get_articles()
    for a in articles:
        a.html_short = shorten_html(a.html, HTML_SHORTEN_LENGTH)
    return render_to_response('planet/index.html', RequestContext(request, {
            'articles': articles,
            'active_tab':'planet',
            }))

@login_required
@csrf_protect
def planet_create(request):
    if request.POST:
        form = PlanetForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.published = datetime.now()
            blog.save()
            return redirect('/planet')
    else:
        form = PlanetForm()

    return render_to_response('planet/create.html', RequestContext(request, {
        'active_tab': 'planet',
        'form': form,
    }))
