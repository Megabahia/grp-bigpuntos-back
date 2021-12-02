from rest_framework import serializers

from apps.CORP.corp_empresas.models import (
    Empresas
)

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = '__all__'
