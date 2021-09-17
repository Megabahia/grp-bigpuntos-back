from rest_framework import serializers

from apps.CENTRAL.central_publicaciones.models import (
    Publicaciones
)

class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
       	fields = '__all__'
