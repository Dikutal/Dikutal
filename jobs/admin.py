from jobs.models import Job, JobAdmin
from django.contrib import admin

admin.site.register(Job, JobAdmin)

