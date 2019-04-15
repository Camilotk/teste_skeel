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
    name = models.CharField(null=False, verbose_name=_(u"Nome"), max_length=50)
    cnpj = models.CharField(null=False, verbose_name="CNPJ", max_length=20)
    description = models.TextField(null=True, verbose_name=_(u"Descrição"))
    location_city = models.CharField(null=False, verbose_name=_(u"Localização"), max_length=50)
    phone = models.CharField(null=True, verbose_name=_(u"Telefone"), max_length=14)
    email = models.EmailField(null=True, verbose_name=_(u"E-mail"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _(u"Empresa")
        verbose_name_plural = _(u"Empresas")

class JobVacancy (models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name=_(u"Título"))
    description = models.TextField(null=False, verbose_name=_(u"Descrição"))
    initial_date = models.DateTimeField(default=timezone.now, verbose_name=_(u"Data Inicial"))
    final_date = models.DateTimeField(blank=True, null=True, verbose_name=_(u"Data Final"))
    initial_salary = models.FloatField(null=False, verbose_name=_(u"Salário Inicial"))
    final_salary = models.FloatField(null=False, verbose_name=_(u"Salário Final"))
    contract_type = models.CharField(choices=CONTRACT_CHOICES, null=False, max_length=50, 
                                     verbose_name=_(u"Tipo de Contrato"))
    status = models.CharField(choices=CHOICE_STATUS, default=ACTIVE, blank=False, max_length=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_(u"Empresa"))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _(u"Vaga")
        verbose_name_plural = _(u"Vagas")


class Benefits(models.Model):
    description = models.TextField(null=False)
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, related_name='benefits_job')

class Requirements(models.Model):
    description = models.TextField(null=False)
    job_vacancy = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, related_name='requirements_job')
