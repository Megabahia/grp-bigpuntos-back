from djongo import models

# Create your models here.
class CreditoPersonas(models.Model):
    _id = models.ObjectIdField()
    monto = models.FloatField(blank=True, null=True)
    plazo = models.PositiveIntegerField(blank=True, null=True)
    aceptaTerminos = models.SmallIntegerField(default=1)
    estado = models.CharField(max_length=255,blank=True, null=True)
    user_id = models.CharField(max_length=255,blank=False, null=False)  # Relacion usuario
    empresaComercial_id = models.CharField(max_length=255,blank=False, null=False)  # Relacion empresa comercial
    empresaIfis_id = models.CharField(max_length=255,blank=False, null=False)  # Relacion empresa ifis
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)