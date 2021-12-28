from rest_framework import serializers

from apps.CORP.corp_creditoPreaprobados.models import (
    CreditoPreaprobados
)

from apps.CORP.corp_empresas.models import Empresas

class CreditoPreaprobadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditoPreaprobados
       	fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        data = super(CreditoPreaprobadosSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        empresa = data.pop('empresa')
        entidadFinanciera = Empresas.objects.filter(_id=empresa, state=1).first()
        data.update({"entidadFinanciera": entidadFinanciera.nombreComercial})
        # data['imagen'] = entidadFinanciera.imagen
        return data
