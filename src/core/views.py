from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from src.departamento.models import Departamento
from src.funcionario.models import Funcionario
from src.registro_hora_extra.models import RegistroHoraExtra

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from src.core.serializers import UserSerializers, GroupSerializers

from django.core import serializers
from django.http import HttpResponse


@login_required()
def home(request):
    data = {}
    data['usuario'] = request.user
    funcionario = request.user.funcionario
    data['total_funcionarios'] = funcionario.empresa.total_funcionarios
    data['total_funcionarios_ferias'] = funcionario.empresa.total_funcionarios_ferias
    data['total_funcionarios_doc_pendente'] = funcionario.empresa.total_funcionarios_doc_pendente
    data['total_funcionarios_doc_ok'] = funcionario.empresa.total_funcionarios_doc_ok
    data['total_funcionarios_rg'] = 10
    data['total_hora_extra_utilizada'] = RegistroHoraExtra.objects.filter(
        funcionario__empresa=funcionario.empresa, utilizada=True).aggregate(Sum('horas'))['horas__sum']
    data['total_hora_extra_pendente'] = RegistroHoraExtra.objects.filter(
        funcionario__empresa=funcionario.empresa, utilizada=False).aggregate(Sum('horas'))['horas__sum']
    return render(request, 'core/index.html', data)


def departamentos_ajax(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos_ajax.html', {'departamentos': departamentos})


def filtra_funcionarios(request):
    depart = request.GET['outro_param']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers