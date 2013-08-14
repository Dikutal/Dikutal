from django import forms
from django.db import models
from django.forms.widgets import DateTimeInput
from jobs.models import Company, Job
from django.core.exceptions import ValidationError

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'content', 'language', 'content_format', 'address', 'hours',
                  'deadline', 'salary', 'company')

# Maybe use RelatedFieldWidgetWrapper to add a '+' after the select box, like on
# the admin site. See
# https://groups.google.com/forum/?fromgroups#!topic/django-users/WVAjV2XY5Go,
# http://stackoverflow.com/questions/38601/using-django-time-date-widgets-in-custom-form,
# and
# https://github.com/django/django/blob/master/django/contrib/admin/widgets.py#L228

    # def __init__(self, *args, **kwargs):
    #     super(JobForm, self).__init__(*args, **kwargs)
    #     self.fields['company'].widget = RelatedFieldWidgetWrapper(
    #         self.fields['company'], rel, admin_site)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'company_description', 'company_contact',
                  'company_email', 'company_address', 'company_phone', 'image')
