from rest_framework import serializers

from apps.CORP.corp_movimientoCobros.models import (
    MovimientoCobros
)

from apps.PERSONAS.personas_personas.models import Personas

class MovimientoCobrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoCobros
       	fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
            data = super(MovimientoCobrosSerializer, self).to_representation(instance)
            # Buscamos la persona y agregamos los campos
            persona = Personas.objects.filter(user_id=instance.user_id).first()
            if persona:
                data.update({"nombres": persona.nombres})
                data.update({"apellidos": persona.apellidos})
                data.update({"identificacion": persona.identificacion})
                data.update({"email": persona.email})
            return data
