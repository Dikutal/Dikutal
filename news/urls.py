from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    (r'^$', 'news_index'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'news_view'),
    (r'^create/', 'news_create'),
    (r'^edit/(?P<id>\d+)/', 'news_edit'),
    (r'^comments/', include('django.contrib.comments.urls')),
)
