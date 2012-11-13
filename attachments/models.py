from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from datetime import datetime

class Attachment(models.Model):
    file = models.FileField(upload_to='uploads')
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def url(self):
        return ('attachments.views.view', (), {
                'id': self.id})

    def get_absolute_url(self):
        return self.url()

class AttachmentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('file', 'description')
        }),
        )
    list_display = ['file', 'description']
