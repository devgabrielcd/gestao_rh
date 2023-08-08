from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from src.departamento.models import Departamento
from src.empresa.models import Empresa
from django.urls import reverse


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    de_ferias = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('list_funcionario')

# somar as horas extras do funcionario logado. o Filter faz faz as horas utilizadas a nao serem contabilizadas
    @property
    def total_hora_extra(self):
        total = self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum']
        return total or 0

    def __str__(self):
        return self.nome
