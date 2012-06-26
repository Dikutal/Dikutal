from django.db import models
from django.contrib import admin

class Article(models.Model):
    title = models.CharField(max_length=300)
    teaser = models.TextField()
    content = models.TextField()
    #author = models.ForeignKey(User, related_name='%(class)ss')
    published = models.DateTimeField()
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    @models.permalink
    def url(self):
        return ('news.views.article_view', (), {
            'id': self.id,
            'slug': self.slug})


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class NewsArticle(Article):
    event_date = models.DateField(null=True)
    event_location = models.CharField(max_length=100, null=True)


class NewsArticleAdmin(ArticleAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'teaser', 'content', 'published', 'slug')
        }),
        ('Event details', {
            'classes': ('collapse', ),
            'description': 'Articles with an event date will be showed in the calendar.',
            'fields': ('event_date', 'event_location')
        }),
    )
