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


class GenderViewSet(viewsets.ModelViewSet):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class AdressViewSet(viewsets.ModelViewSet):
    queryset = models.Adress.objects.all()
    serializer_class = serializers.AdressSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class IndividualClientDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.IndividualClientDetails.objects.all()
    serializer_class = serializers.IndividualClientDetailsSerializer


class CompanyClientDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.CompanyClientDetails.objects.all()
    serializer_class = serializers.CompanyClientDetailsSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class GearboxTypeViewSet(viewsets.ModelViewSet):
    queryset = models.GearboxType.objects.all()
    serializer_class = serializers.GearboxTypeSerializer


class FuelTypeViewSet(viewsets.ModelViewSet):
    queryset = models.FuelType.objects.all()
    serializer_class = serializers.FuelTypeSerializer


class CarCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.CarCategory.objects.all()
    serializer_class = serializers.CarCategorySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseSerializer


class InsurancePolicyViewSet(viewsets.ModelViewSet):
    queryset = models.InsurancePolicy.objects.all()
    serializer_class = serializers.InsurancePolicySerializer
