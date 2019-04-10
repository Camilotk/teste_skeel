from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^vagas/nova', CreateJobVacancy.as_view()),
]
