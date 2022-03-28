from rest_framework import serializers
# ObjectId
from bson import ObjectId

from apps.CORP.corp_creditoArchivos.models import (
    PreAprobados,
)

class CreditoArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAprobados
       	fields = '__all__'
        read_only_fields = ['_id']
