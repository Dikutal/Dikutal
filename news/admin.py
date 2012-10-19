from news.models import Article, ArticleAdmin
from django.contrib import admin

admin.site.register(Article, ArticleAdmin)

