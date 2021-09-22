from rest_framework import serializers

from apps.PERSONAS.personas_personas.models import (
    Personas, ValidarCuenta
)

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
       	fields = '__all__'

class PersonasUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'
        read_only_fields = ['user_id']

class PersonasImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personas
        fields = ['imagen','updated_at']

class ValidarCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidarCuenta
       	fields = '__all__'


