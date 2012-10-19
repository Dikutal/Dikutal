from django import template
from django.utils.html import escape
import urllib, hashlib

register = template.Library()

@register.simple_tag
def gravatar_url(email, size=80):
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'s':str(size)})
    return gravatar_url

@register.simple_tag
def gravatar(email, size=80):
    url = gravatar_url(email, size)
    return """<img class="gravatar" src="%s" height="%s" width="%s"/>""" % (escape(url), size, size)

