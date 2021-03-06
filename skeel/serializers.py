from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import *

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements 
        fields = ["id", "description"]

class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = ["id", "description"]

class JobVacancySerializer(WritableNestedModelSerializer):
    benefits_job = BenefitsSerializer(many=True)
    requirements_job = RequirementsSerializer(many=True)
    class Meta:
        model = JobVacancy
        fields = ["id", "title", "description", "initial_date", "final_date",
                  "initial_salary", "final_salary","contract_type", "status",
                  "company", "requirements_job", "benefits_job"]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "cnpj", "location_city", "phone", "description", "email"]
