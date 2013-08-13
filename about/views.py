from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, Template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from datetime import datetime
from markdown import markdown
from settings import *
from util.modtemplate import *

about_template = mod_template('about/index.md', markdown)

def index(request):
    return HttpResponse(about_template.render(RequestContext(request, {})))
