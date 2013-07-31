from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dikucalendar.views',
    (r'^(?P<year>\d+)/(?P<month>\d+)$', 'calendar'),
    (r'^$', 'index'),
)
