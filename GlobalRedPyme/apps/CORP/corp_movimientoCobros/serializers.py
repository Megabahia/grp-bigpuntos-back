from rest_framework import serializers

from .models import (
    MovimientoCobros
)

from ...PERSONAS.personas_personas.models import Personas
from ...PERSONAS.personas_personas.serializers import PersonasSerializer


class MovimientoCobrosSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla MovimientoCobros
    # el campo fields indica los campos que se devolveran
    # el campo read_only_fields
    class Meta:
        model = MovimientoCobros
        fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        """
        Este metod sirve para modificar los datos que se devulveran a frontend
        @type instance: El campo instance contiene el registro de la base datos
        @rtype: Devuelve la informacion modificada
        """
        data = super(MovimientoCobrosSerializer, self).to_representation(instance)
        # Buscamos la persona y agregamos los campos
        persona = Personas.objects.filter(user_id=instance.user_id).first()
        personaSerializer = PersonasSerializer(persona).data
        if personaSerializer:
            data.update({"nombres": personaSerializer['nombres']})
            data.update({"apellidos": personaSerializer['apellidos']})
            data.update({"identificacion": personaSerializer['identificacion']})
            data.update({"email": personaSerializer['email']})
        return data
