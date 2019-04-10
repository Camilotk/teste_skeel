from rest_framework import serializers
from .models import *

class JobVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobVacancy
        fields = ["id", "title", "description", "initial_date", "final_date", "initial_salary", "final_salary","contract_type", "status"]
