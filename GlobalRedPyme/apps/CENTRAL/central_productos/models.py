from djongo import models


# Create your models here.
class Productos(models.Model):
    _id = models.ObjectIdField()
    nombre = models.TextField(max_length=200,null=False, blank=False)
    marca = models.CharField(max_length=255,null=False, blank=False)
    imagen = models.TextField(max_length=200,null=True, blank=True)
    precioNormal = models.FloatField(null=False, blank=False)
    precioSupermonedas = models.CharField(max_length=200,null=False, blank=False)
    efectivo = models.FloatField(null=False, blank=False)
    codigoQR = models.CharField(max_length=200,null=True, blank=True)
    cantidad = models.IntegerField(null=False, blank=False)
    empresa_id = models.CharField(max_length=200, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)