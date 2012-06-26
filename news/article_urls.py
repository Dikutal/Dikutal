from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    (r'^$', 'article_index'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'article_view'),
    (r'^comments/', include('django.contrib.comments.urls')),
)
