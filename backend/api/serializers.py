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
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class AdressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Adress
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Client
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)


class IndividualClientDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IndividualClientDetails
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)


class CompanyClientDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CompanyClientDetails
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Position
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class GearboxTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.GearboxType
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class FuelTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FuelType
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class CarCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CarCategory
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Car
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.House
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)

class InsurancePolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InsurancePolicy
        generated_fields = SerializerMethods.generate_columns_from_model(model)
        fields = ('url', *generated_fields)