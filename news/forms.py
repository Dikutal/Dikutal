from django import forms
from django.forms.widgets import DateTimeInput
from news.models import Article
from attachments.models import Attachment
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'teaser', 'content', 'front_image',
                  'event_start', 'event_end', 'event_location')
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['front_image'].widget = widgets.RelatedFieldWidgetWrapper(
            self.fields['front_image'].widget,
            Article._meta.get_field('front_image').rel,
            Article.admin_site)
