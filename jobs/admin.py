from jobs.models import Job, JobAdmin, JobFeed, JobFeedAdmin
from django.contrib import admin

admin.site.register(Job, JobAdmin)
admin.site.register(JobFeed, JobFeedAdmin)

