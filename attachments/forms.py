from django import forms
from django.forms.widgets import DateTimeInput
from attachments.models import Attachment
from django.core.exceptions import ValidationError

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('file', 'description')
