from rest_framework import serializers
# ObjectId
from bson import ObjectId

from ...CORP.corp_empresas.models import Empresas
from ...CORP.corp_empresas.serializers import EmpresasSerializer

from ...CENTRAL.central_productos.models import (
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
            data['empresa_id'] = empresa_id
            data['empresa'] = empresa.nombreComercial
            data['local'] = empresa.direccion
            data['pais'] = empresa.pais
            data['provincia'] = empresa.provincia
            data['ciudad'] = empresa.ciudad
            data['imagen_empresa'] = EmpresasSerializer(empresa).data['imagen']
        return data


class ProductosImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['imagen', 'updated_at']


class ProductosLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProductosLandingSerializer, self).to_representation(instance)
        empresa_id = data.pop('empresa_id')
        # empresa = EmpresasCenter.objects.get(pk=ObjectId(empresa_id))
        # print(empresa)
        # if empresa:
        #     data['empresa_id'] = empresa_id
        #     data['empresa'] = empresa.nombre
        #     data['bigPuntos'] = empresa.bigPuntos
        #     data['logo'] = EmpresasLandingSerializer(empresa).data['logo']
        return data
