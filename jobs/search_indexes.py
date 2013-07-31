import datetime
from haystack import indexes
from jobs.models import Company, Job


class CompanyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # name = indexes.CharField(model_attr='company_name')

    def get_model(self):
        return Company


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # company = indexes.CharField(model_attr='company')
    # title = indexes.CharField(model_attr='title')
    # published = indexes.DateTimeField(model_attr='published')

    def get_model(self):
        return Job

    # def index_queryset(self):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(published__lte=datetime.datetime.now())
