import json
import requests
from .forms import *
from django.shortcuts import render
from django.template.defaulttags import register
from skeel.models import Company
from django.utils import timezone
from django.core.paginator import Paginator

def job_list(request, page_number=1):
    response = requests.get('http://127.0.0.1:8000/api/vagas/lista/?page={}'.format(page_number))
    results = response.json()
    jobs = results['results']
    actual_page = int(page_number)
    companies = Company.objects.all()
    return render(request, 'page/job_list.html', {
        'jobs': results,
        'data': jobs,
        'previous_page': actual_page - 1,
        'next_page': actual_page + 1,
        'companies': companies,
    })

def job_new(request):
    form = JobForm()
    return render(request, 'page/job_edit.html', {'form': form})

def company_new(request):
    form = CompanyForm()
    return render(request, 'page/company_edit.html', {'form': form})
