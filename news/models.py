from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=300)
    teaser = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, related_name='%(class)ss') # TODO: integrate with OSQA
    published = models.DateTimeField(blank=True, null=True)
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads')
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)
    event_location = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def url(self):
        return ('news.views.news_view', (), {
            'id': self.id,
            'slug': self.slug})

    def get_absolute_url(self):
        return self.url()


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'teaser', 'content', 'published', 'slug')
        }),
        ('Event details', {
            'classes': ('collapse', ),
            'description': 'Articles with an event date will be showed in the calendar.',
            'fields': ('event_start', 'event_end', 'event_location')
        }),
        )