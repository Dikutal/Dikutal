from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from settings import *

def index(request):
    return render_to_response('about/index.html', RequestContext(request, {}))
