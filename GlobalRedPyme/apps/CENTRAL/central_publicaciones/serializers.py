from rest_framework import serializers

from apps.CENTRAL.central_publicaciones.models import (
    Publicaciones
)

class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
       	fields = '__all__'

class PublicacionesImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicaciones
        fields = ['imagen','updated_at']