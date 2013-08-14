import os.path

from django.template import RequestContext, Template

pre = '''
{% extends "master.html" %}

{% load markup %}

{% block content %}
'''

post = '''
{% endblock content %}
'''

def mod_template(path, func):
    with open(os.path.join('templates', path)) as f:
        text = f.read().decode('utf-8')
    return Template(pre + func(text) + post)
