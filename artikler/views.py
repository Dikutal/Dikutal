from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseForbidden, Http404, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from news.models import Article

def artikel_view(request, slug):
    articles = Article.objects.filter(slug=slug)
    if not articles:
        raise Http404("Invalid slug")
    else:
        return HttpResponsePermanentRedirect("/news/%s/%s" % (articles[0].id, slug))
