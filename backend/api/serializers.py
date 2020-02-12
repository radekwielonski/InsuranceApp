from rest_framework import serializers
from django.contrib.auth.models import User
from api import models


class SerializerMethods():
    @staticmethod
    def generate_columns_from_model(model):
        list_of_attributes = []

        for f in model._meta.get_fields():
            list_of_attributes.append(f.name)

        return list_of_attributes[1:]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gender
        fields = ('url', 'gender')


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
