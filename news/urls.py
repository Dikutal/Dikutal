from django.conf.urls.defaults import patterns, include, url
from django.contrib.syndication.views import Feed
from news.models import Article

class LatestArticles(Feed):
    title = "Dikutal's articles"
    link = "/news/"
    description = "The newest articles from Dikutal"

    def items(self):
        return Article.objects.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser

urlpatterns = patterns('news.views',
    (r'^$', 'news_index'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'news_view'),
    (r'^create/', 'news_create'),
    (r'^edit/(?P<id>\d+)/', 'news_edit'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^feed/$', LatestArticles()),
    (r'^ical/$', LatestArticlesIcal()),
)
