from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from django.contrib.syndication.views import Feed
from jobs.models import Job

class LatestJobs(Feed):
    title = "Jobs listed on Dikutal"
    link = "/jobs/"
    description = "The newest jobs listed on Dikutal"

    def items(self):
        return Job.objects.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

urlpatterns = patterns('jobs.views',
    (r'^$', 'index'),
    (r'create/', 'create'),
    (r'create-company/', 'create_company'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'jobs_view'),
    (r'^companies/(?P<id>\d+)$', 'companies_view'),
    (r'^feed/$', LatestJobs()),
)
