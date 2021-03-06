import datetime
from haystack import indexes
from news.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # author = indexes.CharField(model_attr='author')
    # published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Article

    # def index_queryset(self):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.all() #filter(published__lte=datetime.datetime.now())
