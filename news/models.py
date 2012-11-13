from django.db import models
from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter
from django.contrib.auth.models import User
from django.db.models import Q
from attachments.models import Attachment

from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=300)
    teaser = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, related_name='%(class)ss') # TODO: integrate with OSQA
    published = models.DateTimeField(blank=True, null=True)
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    front_image = models.ForeignKey(Attachment, null=True, blank=True)
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

    def can_edit(self, user):
        return user == self.author or user.is_staff

    def is_published(self):
        return self.published is not None and self.published <= datetime.now()
    is_published.boolean = True
    is_published.admin_order_field = 'published'

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'teaser', 'content', 'front_image', 'published', 'slug')
        }),
        ('Event details', {
            'classes': ('collapse', ),
            'description': 'Articles with an event date will be showed in the calendar.',
            'fields': ('event_start', 'event_end', 'event_location')
        }),
        )
    actions = ['publish', 'unpublish']
    list_display = ['title', 'slug', 'author', 'created', 'last_edited', 'is_published']
    list_filter = ('author__username', 'published')
    search_fields = ['title', 'author__username', 'teaser', 'content', 'event_location']
    
    def __init__(self, model, admin_site):
        super(ArticleAdmin, self).__init__(model, admin_site)
        Article.admin_site = admin_site
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(ArticleAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form

    def publish(modeladmin, request, queryset):
        queryset.filter(published=None).update(published=datetime.now())

    def unpublish(modeladmin, request, queryset):
        queryset.update(published=None)
