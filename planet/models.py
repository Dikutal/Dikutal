from django.db import models
from django.contrib import admin

class PlanetFeed(models.Model):
    url = models.URLField()
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url

class PlanetFeedAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('url',)
        }),
        )

