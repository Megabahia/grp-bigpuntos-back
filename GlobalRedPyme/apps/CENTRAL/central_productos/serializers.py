from rest_framework import serializers
# ObjectId
from bson import ObjectId

from apps.CORP.corp_empresas.models import Empresas

from apps.CENTRAL.central_productos.models import (
    Productos
)

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
       	fields = '__all__'

    def to_representation(self, instance):
        data = super(ProductosSerializer, self).to_representation(instance)
        empresa_id = data.pop('empresa_id')
        empresa = Empresas.objects.get(pk=ObjectId(empresa_id))
        if empresa:
            data['empresa'] = empresa.nombre
            data['local'] = empresa.local
            data['provincia'] = empresa.provincia
            data['ciudad'] = empresa.ciudad
        return data

class ProductosImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['imagen','updated_at']
