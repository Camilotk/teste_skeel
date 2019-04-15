import json
import requests
from django.shortcuts import render
from django.template.defaulttags import register
from skeel.models import JobVacancy
from django.utils import timezone

def job_list(request):
    jobs = JobVacancy.objects.filter(initial_date__lte=timezone.now()).order_by('initial_date')
    return render(request, 'page/job_list.html', {"jobs": jobs})

