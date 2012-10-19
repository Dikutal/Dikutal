from django import forms
from django.forms.widgets import DateTimeInput
from jobs.models import Company, Job
from django.core.exceptions import ValidationError

# Maybe use BetterModelForm from https://github.com/carljm/django-form-utils ?
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'content', 'address', 'hours', 'deadline', 'salary', 'company')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'company_description', 'company_contact',
                  'company_email', 'company_address', 'company_phone')
