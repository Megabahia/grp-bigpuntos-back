from rest_framework import serializers

from apps.PYMES.pymes_empresas.models import (
    Empresas
)

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
       	fields = '__all__'
