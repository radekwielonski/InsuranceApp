from rest_framework import serializers
from api.simple_serializer import SimpleSerializer
from django.contrib.auth.models import User
from api import models
from django.db.models import ForeignKey, ManyToOneRel, ManyToManyRel, ManyToManyField


class SerializerMethods():
    @staticmethod
    def generate_columns_from_model(model):
        list_of_attributes = []
        for field in model._meta.get_fields():
            if field.name != 'id' and not isinstance(field, ManyToOneRel):
                list_of_attributes.append(field.name)

        return list_of_attributes


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gender
        fields = '__all__'


class AdressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Adress
        fields = '__all__'


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class IndividualClientDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndividualClientDetails
        fields = '__all__'


class CompanyClientDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CompanyClientDetails
        fields = '__all__'


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class GearboxTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GearboxType
        fields = '__all__'


class FuelTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FuelType
        fields = '__all__'


class CarCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CarCategory
        fields = '__all__'


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Car
        fields = '__all__'


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.House
        fields = '__all__'


class InsurancePolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InsurancePolicy
        fields = '__all__'
