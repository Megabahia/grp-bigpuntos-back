from rest_framework import serializers

from .models import (
    Pagos
)

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
       	fields = '__all__'
        read_only_fields = ['_id']