from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('vaga/nova/', views.job_new, name='job_edit'),
    path('empresa/nova/', views.company_new, name='company_edit'),
    url(r'^p/(?P<page_number>[0-9]+)/$', views.job_list, name="pages"),
]
