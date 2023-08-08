
from rest_framework import serializers
from src.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']