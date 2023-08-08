from rest_framework import viewsets
from src.funcionario.api.serializers import FuncionarioSerializers
from src.funcionario.models import Funcionario
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

