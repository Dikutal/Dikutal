from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('about.views',
    (r'^$', 'index'),
)
