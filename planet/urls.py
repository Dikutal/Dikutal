from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('planet.views',
    (r'^$', 'index'),
    (r'^overview$', 'overview'),
    (r'^create/', 'planet_create'),
)
