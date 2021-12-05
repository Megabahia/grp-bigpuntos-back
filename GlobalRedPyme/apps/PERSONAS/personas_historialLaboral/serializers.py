from rest_framework import serializers

from apps.PERSONAS.personas_historialLaboral.models import (
    HistorialLaboral
)

class HistorialLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialLaboral
       	fields = '__all__'
        read_only_fields = ['_id']

    def to_representation(self, instance):
        data = super(HistorialLaboralSerializer, self).to_representation(instance)
        # tomo el campo persona y convierto de OBJECTID a string
        persona = str(data.pop('persona'))
        data.update({"persona": persona})
        return data