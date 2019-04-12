from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^vagas/nova/$', CreateJobVacancy.as_view()),
        url(r'^vagas/lista/$', ListJobVacancy.as_view()),
        url(r'^vagas/lista/(?P<pk>[0-9]+)/$', GetJobByID.as_view()),
        url(r'^vagas/editar/(?P<pk>[0-9]+)/$', EditJobByID.as_view()),
        url(r'^vagas/deletar/(?P<pk>[0-9]+)/$', DeleteJobByID.as_view()),
]
