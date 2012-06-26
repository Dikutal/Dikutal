from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    (r'^$', 'index'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'view'),
    (r'^comments/', include('django.contrib.comments.urls')),
)
