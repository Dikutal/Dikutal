from jobs.models import Company, CompanyAdmin, Job, JobAdmin, JobFeed, JobFeedAdmin
from django.contrib import admin

admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobFeed, JobFeedAdmin)

