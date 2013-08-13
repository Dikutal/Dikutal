from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('planet.views',
    (r'^$', 'index'),
    (r'^create/', 'planet_create'),
)
