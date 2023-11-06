"""Nube Bigpuntos
PORTALES: CENTER, PERSONAS, CORP, IFIS
"""

from rest_framework import serializers

from .models import Empresas

# La clase EmpresasSerializer se utiliza para conectar con el modelo Empresas de la base de datos central
class EmpresasSerializer(serializers.ModelSerializer):
    # El campo model se conecta con la tabla Empresas de la base da tos central
    # el campo fields se usa para escoger los campos de las empresas
    # El campo read_only_fields solo permite la lectura
    class Meta:
        model = Empresas
        fields = '__all__'
        read_only_fields = ['_id']
