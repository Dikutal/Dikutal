from django.db import models
from django.contrib import admin
from datetime import datetime
import util.formats as formats
from django.contrib.auth.models import User

class Company(models.Model):
    # Company concact info
    company_name = models.CharField(max_length=100,blank=True)
    company_description = models.TextField(blank=True)
    company_contact = models.CharField("Contact name", max_length=100, blank=True)
    company_email = models.CharField(max_length=100, blank=True)
    company_address = models.TextField(blank=True)
    company_phone = models.CharField(max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='%(class)ss')

    def __unicode__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'companies'

    @models.permalink
    def url(self):
        return ('jobs.views.companies_view', (), {
                'id': self.id})

    def get_absolute_url(self):
        return self.url()

    def can_edit(self, user):
        return user == self.author or user.is_staff
        

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('author', 'company_name', 'company_address',
                       'company_description', 'company_contact',
                       'company_email', 'company_phone')
        }),
    )
    list_display = ['company_name', 'company_contact', 'company_email', 'company_phone']
    list_filter = ['company_name']


class Job(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    content_format = models.CharField(
        max_length=2, choices=formats.FORMATS, default=formats.DEFAULT)
    author = models.ForeignKey(User, related_name='%(class)ss')
    published = models.DateTimeField(blank=True, null=True)
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField()

    # Job info
    address = models.TextField(blank=True, null=True)
    hours = models.CharField(max_length=50, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    salary = models.CharField(max_length=50, blank=True, null=True)

    # Company
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return self.title

    @models.permalink
    def url(self):
        return ('jobs.views.jobs_view', (), {
                'id': self.id,
                'slug': self.slug})

    def get_absolute_url(self):
        return self.url()

    def can_edit(self, user):
        return user == self.author or user.is_staff

    def is_shown(self):
        now = datetime.now()
        return (self.published is not None
                and (self.deadline is None or
                     (self.published <= now
                      and self.deadline > now)))
    is_shown.boolean = True
    is_shown.admin_order_field = 'published'

    def is_published(self):
        return self.published is not None and self.published <= datetime.now()
    is_published.boolean = True
    is_published.admin_order_field = 'published'


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        (None, {
            'fields': ('author', 'title', 'content', 'content_format', 'published', 'company', 'slug')
        }),
        ('Job info', {
            'description': "Application information for the job. Leave address out to use the company's address.",
            'fields': ('address', 'hours', 'deadline', 'salary')
        }),
    )
    list_display = ['title', 'company', 'salary', 'is_shown', 'is_published']
    list_filter = ['company', 'published', 'deadline']
    actions = ['publish', 'unpublish']

    def publish(modeladmin, request, queryset):
        queryset.filter(published=None).update(published=datetime.now())

    def unpublish(modeladmin, request, queryset):
        queryset.update(published=None)
    
class JobFeed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url

class JobFeedAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'url')
        }),
        )
    list_display = ['title', 'url']
