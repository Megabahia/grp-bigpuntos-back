from rest_framework import serializers
# ObjectId
from bson import ObjectId

from apps.CORP.corp_creditoPreaprobados.models import (
    CreditoPreaprobados
)

from apps.CORP.corp_empresas.models import Empresas
from apps.PERSONAS.personas_personas.models import Personas

class CreditoPreaprobadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditoPreaprobados
       	fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        data = super(CreditoPreaprobadosSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        empresa_financiera = data.pop('empresa_financiera')
        entidadFinanciera = Empresas.objects.filter(_id=empresa_financiera, state=1).first()
        data.update({"entidadFinanciera": entidadFinanciera.nombreComercial})
        data['empresa_financiera'] = str(empresa_financiera)
        # data['imagen'] = entidadFinanciera.imagen
        # Informacion persona
        persona = Personas.objects.filter(user_id=str(instance.user_id),state=1).first()
        if persona is not None:
            data.update({"nombres": persona.nombres})
            data.update({"apellidos": persona.apellidos})
        return data
