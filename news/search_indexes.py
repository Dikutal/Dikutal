import datetime
from haystack import indexes
from news.models import Article

class ArticleIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    text = indexes.CharField(model_attr='content', document=True)
    author = indexes.CharField(model_attr='author')
    published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Article

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published__lte=datetime.datetime.now())
