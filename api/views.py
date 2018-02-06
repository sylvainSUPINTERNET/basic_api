from django.shortcuts import render

from django.contrib.auth.models import User, Group, Permission
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PermissionSerializer, SpellSerializer
from api.models import Spell
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response




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


class SpellList(APIView):
    """
    List all spells, or create a new spell.
    """
    def get(self, request, format=None):
        spell = Spell.objects.all()
        serializer = SpellSerializer(spell, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpellDetails(APIView):
    """
    Retrieve, update or delete a spell instance.
    """
    def get_object(self, pk):
        try:
            return Spell.objects.get(pk=pk)
        except Spell.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spell = self.get_object(pk)
        serializer = SpellSerializer(spell)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spell = self.get_object(pk)
        serializer = SpellSerializer(spell, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spell = self.get_object(pk)
        spell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)