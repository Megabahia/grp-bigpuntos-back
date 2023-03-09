from rest_framework import serializers

from .models import (
    Publicaciones, CompartirPublicaciones
)

from ...PERSONAS.personas_personas.models import Personas


class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
        fields = '__all__'


class PublicacionesImagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicaciones
        fields = ['imagen', 'updated_at']


class CompartirPublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompartirPublicaciones
        fields = '__all__'

    def to_representation(self, instance):
        data = super(CompartirPublicacionesSerializer, self).to_representation(instance)
        # publicacion
        publicacion = str(data.pop('publicacion'))
        data.update({"publicacion": publicacion})
        # user
        user = str(data.pop('user'))
        data.update({"user": user})
        return data


class ListCompartirPublicacionesSerializer(serializers.ModelSerializer):
    publicacion = PublicacionesSerializer(many=False, read_only=True)

    class Meta:
        model = CompartirPublicaciones
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ListCompartirPublicacionesSerializer, self).to_representation(instance)
        # user
        data.pop('user')
        return data


class PublicacionesSinCompartirSerializer(serializers.ModelSerializer):
    publicacion = PublicacionesSerializer(many=False, read_only=True)

    class Meta:
        model = CompartirPublicaciones
        fields = ['publicacion', 'created_at', '_id']

    def to_representation(self, instance):
        data = super(PublicacionesSinCompartirSerializer, self).to_representation(instance)
        # publicacion
        publicacion = data.pop('publicacion')
        data['created_at_compartir'] = data.pop('created_at')
        data['_id'] = publicacion['_id']
        data['titulo'] = publicacion['titulo']
        data['subtitulo'] = publicacion['subtitulo']
        data['descripcion'] = publicacion['descripcion']
        data['imagen'] = publicacion['imagen']
        data['created_at'] = publicacion['created_at']
        data['updated_at'] = publicacion['updated_at']
        data['state'] = publicacion['state']
        return data


class CompartirPublicacionesReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompartirPublicaciones
        fields = ['user', 'publicacion', 'created_at']

    def to_representation(self, instance):
        data = super(CompartirPublicacionesReporteSerializer, self).to_representation(instance)
        # publicacion
        publicacion = Publicaciones.objects.get(pk=data.pop('publicacion'))
        if publicacion is not None:
            data.update({"publicacion_titulo": publicacion.titulo})
            data.update({"publicacion_imagen": PublicacionesImagenSerializer(publicacion).data['imagen']})
        try:
            # user
            persona = Personas.objects.get(user_id=str(data.pop('user')))
            if persona is not None:
                data.update({"nombres": persona.nombres})
                data.update({"apellidos": persona.apellidos})
                data.update({"whatsapp": persona.whatsapp})
                data.update({"email": persona.email})
        except Personas.DoesNotExist:
            data.update({"nombres": ""})
            data.update({"apellidos": ""})
            data.update({"whatsapp": ""})
            data.update({"email": ""})

        return data
