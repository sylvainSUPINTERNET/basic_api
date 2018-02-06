from django.shortcuts import render

from django.contrib.auth.models import User, Group, Permission
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PermissionSerializer, SpellSerializer
from api.models import Spell


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer



class SpellViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows spells to be viewed or edited.
    """
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer