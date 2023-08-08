
from rest_framework import serializers
from src.funcionario.models import Funcionario


class FuncionarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['user', 'nome', 'departamento', 'empresa']