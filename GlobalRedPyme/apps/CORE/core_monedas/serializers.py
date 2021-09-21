from rest_framework import serializers

from apps.CORE.core_monedas.models import (
    Monedas
)

class MonedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monedas
       	fields = '__all__'