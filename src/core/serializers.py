from django.contrib.auth.models import User, Group
from rest_framework import serializers
from src.funcionario.models import Funcionario


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        Fields = ['url', 'name']