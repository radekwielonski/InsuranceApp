from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from api import serializers, models

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer