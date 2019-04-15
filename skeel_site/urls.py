from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/new/', views.job_new, name='job_edit'),
    path('company/new/', views.company_new, name='company_edit'),
]
