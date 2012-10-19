from django.conf.urls.defaults import patterns, include, url
from django.contrib.syndication.views import Feed
from django.contrib import admin
from news.models import Article
import settings

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


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),

    url(r'^$', 'frontpage.views.index', name='frontpage'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^jobs/', include('jobs.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^planet/', include('planet.urls')),

    url(r'^news/feed/$', LatestArticles()),
)
