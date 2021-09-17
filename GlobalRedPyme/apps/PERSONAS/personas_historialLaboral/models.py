from djongo import models
from apps.PERSONAS.personas_personas.models import Personas


# Create your models here.
class HistorialLaboral(models.Model):
    _id = models.ObjectIdField()
    fechaInicio = models.DateField(null=True)
    empresa = models.CharField(max_length=200,null=False)
    tiempoTrabajo = models.SmallIntegerField(null=True)
    cargoActual = models.CharField(max_length=200,null=False)
    estado = models.CharField(max_length=200,null=False)
    persona = models.ForeignKey(Personas, null=False, on_delete=models.DO_NOTHING)  # Relacion Con la categoria

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)