from rest_framework import serializers

from apps.CORP.corp_creditoPersonas.models import (
    CreditoPersonas,
)

class CreditoPersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditoPersonas
       	fields = '__all__'
        read_only_fields = ['_id']