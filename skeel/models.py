from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

ACTIVE = 'A'
INACTIVE = 'I'
CHOICE_STATUS = (
    ('N', _(u"Não Iniciada")),
    ('A', _(u"Em Andamento")),
    ('C', _(u"Concluida")),
)

CONTRACT_CHOICES = (
    ('PJ', _(u"Pessoa Jurídica")),
    ('CLT', _(u"Consolidação das Leis de Trabalho"))
)

class Company(models.Model):
    name = models.CharField(null=False, max_length=50)
    cnpj = models.CharField(null=False, max_length=20)
    description = models.TextField(null=True)
    location_city = models.CharField(null=False, max_length=50)
    phone = models.CharField(null=True, max_length=14)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class JobVacancy (models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    initial_date = models.DateTimeField(default=timezone.now)
    final_date = models.DateTimeField(blank=True, null=True)
    initial_salary = models.FloatField(null=False)
    final_salary = models.FloatField(null=False)
    contract_type = models.CharField(choices=CONTRACT_CHOICES, null=False, max_length=50)
    status = models.CharField(choices=CHOICE_STATUS, default=ACTIVE, blank=False, max_length=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Benefits(models.Model):
    description = models.TextField(null=False)
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, related_name='benefits_job')

class Requirements(models.Model):
    description = models.TextField(null=False)
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, related_name='requirements_job')
