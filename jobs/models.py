from django.db import models
from django.contrib import admin

class Job(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    #author = models.ForeignKey(User, related_name='%(class)ss')
    published = models.DateTimeField()
    last_edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField()

    # Job info
    address = models.TextField()
    hours = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    salary = models.CharField(max_length=50)

    # Company concact info
    company_name = models.CharField(max_length=100,blank=True)
    company_description = models.TextField(blank=True)

    company_contact = models.CharField("Contact name", max_length=100, blank=True)
    company_email = models.CharField(max_length=100, blank=True)
    company_address = models.TextField(blank=True)
    company_phone = models.CharField(max_length=100, blank=True)


    def __unicode__(self):
        return self.title


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'published', 'slug')
        }),
        ('Job info', {
            'classes': ('collapse', ),
            'description': 'Application information for the job.',
            'fields': ('address', 'hours', 'deadline', 'salary')
        }),
        ('Company info', {
            'classes': ('collapse', ),
            'description': 'Information about the company.',
            'fields': ('company_name', 'company_address', 'company_description',
                        'company_contact', 'company_email',
                        'company_phone')
        }),
    )

