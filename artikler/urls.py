from django.conf.urls.defaults import patterns, include, url
from django.contrib.syndication.views import Feed

urlpatterns = patterns('artikler.views',
    (r'^(?P<slug>.*)$', 'artikel_view'),
)
