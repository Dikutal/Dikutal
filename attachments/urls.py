from django.conf.urls.defaults import patterns, include, url
from django.contrib.syndication.views import Feed
from attachments.models import Attachment

urlpatterns = patterns('attachments.views',
    (r'^$', 'attachments_index'),
    (r'^(?P<id>\d+)/$', 'view'),
    (r'^create/', 'attachments_create'),
    (r'^edit/(?P<id>\d+)/', 'attachments_edit'),
)
