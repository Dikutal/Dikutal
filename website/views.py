from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('websits/index.html')

def easteregg(request):
    # TODO
    pass
