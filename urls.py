from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings

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
    url(r'^artikler/', include('artikler.urls')), # for legacy links
    url(r'^planet/', include('planet.urls')),
    url(r'^calendar/', include('dikucalendar.urls')),
    url(r'^attachments/', include('attachments.urls')),
    url(r'^search/', include('haystack.urls')),
)
