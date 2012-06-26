from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    (r'^$', 'news_index'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'news_view'),
    (r'^comments/', include('django.contrib.comments.urls')),
)
