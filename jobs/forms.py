from django import forms
from django.forms.widgets import DateTimeInput
from jobs.models import Job
from django.core.exceptions import ValidationError

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'content', 'address', 'hours', 'deadline', 'salary')
