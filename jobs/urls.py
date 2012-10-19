from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from jobs.models import Job

urlpatterns = patterns('jobs.views',
    (r'^$', 'index'),
    # url(r'^$',
    #     ListView.as_view(
    #         queryset=Job.objects.order_by('-published')[:5],
    #         template_name='jobs/index.html')),
    (r'create/', 'create'),
    (r'create-company/', 'create_company'),
    (r'^(?P<id>\d+)/(?P<slug>.*)$', 'jobs_view'),
    # url(r'^(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model=Job,
    #         template_name='jobs/detail.html')),
    #url(r'^(?P<pk>\d+)/results/$',
    #    DetailView.as_view(
    #        model=Poll,
    #        template_name='polls/results.html'),
    #    name='poll_results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)
