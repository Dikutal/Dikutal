import os.path

from django.template import RequestContext, Template

def mod_template(path, func):
    with open(os.path.join('templates', path)) as f:
        text = f.read().decode('utf-8')
    return Template(func(text))
