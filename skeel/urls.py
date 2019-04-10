from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^vagas$', ListJobVacancy.as_view()),
]
