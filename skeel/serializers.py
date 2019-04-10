from rest_framework import serializers
from .models import *

class JobVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobVacancy
        fields = ["id", "title", "description", "salary", "contract_type", "status"]
