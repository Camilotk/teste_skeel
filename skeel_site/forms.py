from django import forms
from skeel.models import *
from django.utils.translation import ugettext_lazy as _

class JobForm(forms.ModelForm):
    class Meta:
        model = JobVacancy
        fields = ["title", "description", "initial_date", "final_date","initial_salary", 
                "final_salary","contract_type", "status", "company", ]

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "cnpj", "location_city", "phone", "description", "email"]
