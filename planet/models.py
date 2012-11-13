from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from util.feedparsing import get_feed_articles

class PlanetFeed(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField()
    owner = models.ForeignKey(User, related_name='%(class)ss', null=True)
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url

    @staticmethod
    def get_articles():
        return get_feed_articles('planet_articles', PlanetFeed)

class PlanetFeedAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'owner')
        }),
        )
    list_display = ['title', 'url', 'owner']

