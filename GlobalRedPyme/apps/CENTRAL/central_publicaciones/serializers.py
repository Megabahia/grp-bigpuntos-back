from rest_framework import serializers

from .models import (
    Publicaciones, CompartirPublicaciones
)

from ...PERSONAS.personas_personas.models import Personas
from ...PERSONAS.personas_personas.serializers import PersonasSerializer


class PublicacionesSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Publicaciones
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Publicaciones
        fields = '__all__'


class PublicacionesImagenSerializer(serializers.HyperlinkedModelSerializer):
    # La clase meta se relaciona con la tabla Publicaciones
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = Publicaciones
        fields = ['imagen', 'updated_at']


class CompartirPublicacionesSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla Publicaciones
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = CompartirPublicaciones
        fields = '__all__'

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
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

    # La clase meta se relaciona con la tabla Publicaciones
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = CompartirPublicaciones
        fields = '__all__'

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
        data = super(ListCompartirPublicacionesSerializer, self).to_representation(instance)
        # user
        data.pop('user')
        return data


class PublicacionesSinCompartirSerializer(serializers.ModelSerializer):
    publicacion = PublicacionesSerializer(many=False, read_only=True)

    # La clase meta se relaciona con la tabla Publicaciones
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = CompartirPublicaciones
        fields = ['publicacion', 'created_at', '_id']

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
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
    # La clase meta se relaciona con la tabla Publicaciones
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = CompartirPublicaciones
        fields = ['user', 'publicacion', 'created_at']

    def to_representation(self, instance):
        """
        Este metodo se usa para modificar la respuesta de los campos
        @type instance: El campo instance contiene el registro con los campos
        @rtype: DEvuelve los valores modificados
        """
        data = super(CompartirPublicacionesReporteSerializer, self).to_representation(instance)
        # publicacion
        publicacion = Publicaciones.objects.get(pk=data.pop('publicacion'))
        if publicacion is not None:
            data.update({"publicacion_titulo": publicacion.titulo})
            data.update({"publicacion_imagen": PublicacionesImagenSerializer(publicacion).data['imagen']})
        try:
            # user
            persona = Personas.objects.get(user_id=str(data.pop('user')))
            personaSerializer = PersonasSerializer(persona).data
            if personaSerializer is not None:
                data.update({"nombres": personaSerializer.nombres})
                data.update({"apellidos": personaSerializer.apellidos})
                data.update({"whatsapp": personaSerializer.whatsapp})
                data.update({"email": personaSerializer.email})
        except Personas.DoesNotExist:
            data.update({"nombres": ""})
            data.update({"apellidos": ""})
            data.update({"whatsapp": ""})
            data.update({"email": ""})

        return data
