from django.db import models
from django.contrib import admin

class Feed(models.Model):
    url = models.URLField()
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url

class FeedAdmin(admin.ModelAdmin):
    pass

