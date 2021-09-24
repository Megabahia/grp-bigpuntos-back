from rest_framework import serializers
# ObjectId
from bson import ObjectId

from apps.PYMES.pymes_empresas.models import Empresas

from apps.CORE.core_monedas.models import (
    Monedas
)

class MonedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monedas
       	fields = '__all__'

class MonedasUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monedas
       	fields = ['saldo']

class ListMonedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monedas
       	fields = '__all__'

    def to_representation(self, instance):
        data = super(ListMonedasSerializer, self).to_representation(instance)
        empresa_id = data.pop('empresa_id')
        empresa = Empresas.objects.get(pk=ObjectId(empresa_id))
        if empresa:
            data['empresa'] = empresa.nombre
        return data
