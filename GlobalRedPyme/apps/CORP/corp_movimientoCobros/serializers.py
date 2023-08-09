from rest_framework import serializers

from .models import (
    MovimientoCobros
)

from ...PERSONAS.personas_personas.models import Personas
from ...PERSONAS.personas_personas.serializers import PersonasSerializer


class MovimientoCobrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoCobros
        fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
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
