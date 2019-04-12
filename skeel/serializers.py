from rest_framework import serializers
from .models import *

class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Benefits
        fields = ["id", "description", ]

class JobVacancySerializer(serializers.ModelSerializer):
    benefits_jobs = BenefitsSerializer(many=True)
    class Meta:
        model = JobVacancy
        fields = ["id", "title", "description", "initial_date", "final_date", "initial_salary", "final_salary","contract_type", "status", "company", "benefits_jobs"]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "cnpj", "description", "email"]
