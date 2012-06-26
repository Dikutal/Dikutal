from news.models import Article, NewsArticle, ArticleAdmin, NewsArticleAdmin
from django.contrib import admin

admin.site.register(Article, ArticleAdmin)
admin.site.register(NewsArticle, NewsArticleAdmin)

