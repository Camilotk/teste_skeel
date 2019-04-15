import json
import requests
from django.shortcuts import render
from django.template.defaulttags import register
from skeel.models import JobVacancy
from django.utils import timezone

def job_list(request):
    response = requests.get('http://127.0.0.1:8000/api/vagas/lista/')
    results = response.json()
    jobs = results['results']
    return render(request, 'page/job_list.html', {
        'jobs': jobs,
    })

