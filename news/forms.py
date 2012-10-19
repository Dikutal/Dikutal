from django import forms
from django.forms.widgets import DateTimeInput
from news.models import Article
from django.core.exceptions import ValidationError

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'teaser', 'content', 'image',
                  'event_start', 'event_end', 'event_location')
