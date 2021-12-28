from rest_framework import serializers

from apps.CORP.corp_creditoPreaprobados.models import (
    CreditoPreaprobados
)

class CreditoPreaprobadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditoPreaprobados
       	fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        data = super(CreditoPreaprobadosSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        empresa = str(data.pop('empresa'))
        data.update({"empresa": empresa})
        return data
