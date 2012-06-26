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


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class NewsArticle(Article):
    pass


class NewsArticleAdmin(ArticleAdmin):
    pass
