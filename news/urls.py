from django.conf.urls.defaults import patterns, include, url
from django.contrib.syndication.views import Feed
from django_ical.views import ICalFeed
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


class EventArticlesIcal(ICalFeed):

    product_id = '-//dikutal.dk//articles'
    timezone = 'Europe/Copenhagen'
    title = 'Dikutal articles'
    description = 'Articles from dikutal.dk'

    def items(self):
        articles = filter(lambda a: a.has_event(), Article.objects.order_by('-published'))
        return articles

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser

    def item_start_datetime(self, item):
        return item.event_start if item.event_start else item.event_end

    def item_end_datetime(self, item):
        return item.event_end

    def item_link(self, item):
        return 'http://dikutal.dk' + item.url()

        
urlpatterns = patterns('news.views',
    (r'^$', 'news_index'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'news_view'),
    (r'^create/', 'news_create'),
    (r'^edit/(?P<id>\d+)/', 'news_edit'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^feed/$', LatestArticles()),
    (r'^ical/$', EventArticlesIcal()),
)
