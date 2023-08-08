from rest_framework import viewsets
from src.registro_hora_extra.api.serializers import RegistroHoraExtraSerializers
from src.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializers

