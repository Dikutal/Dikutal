from django import forms
from django.forms.widgets import DateTimeInput
from planet.models import PlanetFeed
from attachments.models import Attachment
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class PlanetForm(forms.ModelForm):
    class Meta:
        model = PlanetFeed
        fields = ('title', 'url')
    def __init__(self, *args, **kwargs):
        super(PlanetForm, self).__init__(*args, **kwargs)
