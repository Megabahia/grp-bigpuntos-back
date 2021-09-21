from rest_framework import serializers

from apps.CENTRAL.central_productos.models import (
    Productos
)

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
       	fields = '__all__'
