from django.db import models
from django.utils.translation import ugettext_lazy as _

ACTIVE = 'Y'
INACTIVE = 'N'
CHOICE_ACTIVE = (
    ('Y', _(u"Sim")),
    ('N', _(u"Não")),
)

CONTRACT_CHOICES = (
    ('PJ', _(u"Pessoa Jurídica")),
    ('CLT', _(u"Consolidação das Leis de Trabalho"))
)

class JobVacancy (models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    salary = models.FloatField(null=False)
    contract_type = models.CharField(choices=CONTRACT_CHOICES, null=False, max_length=50)
    status = (max_length=1, choices=CHOICE_ACTIVE, default=ACTIVE, blank=False)

    def __str__(self):
        return self.title
