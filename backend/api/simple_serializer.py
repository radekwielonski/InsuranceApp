from rest_framework import serializers

# TODO create SimpleSerializer which automatically generates fields based on model to simplify serializers.py


class SimpleSerializer(serializers.HyperlinkedModelSerializer):
    def generate_columns_from_model(model):
        pass

        # list_of_attributes = []
        # for f in model._meta.get_fields():
        #     list_of_attributes.append(f.name)

        # return list_of_attributes[1:]

    class Meta:
        pass
