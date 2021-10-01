from djongo import models

def upload_path(instance, filname):
    return '/'.join(['CENTRAL/imgProductos', str(instance._id) + "_" + filname])

# Create your models here.
class Productos(models.Model):
    _id = models.ObjectIdField()
    nombre = models.TextField(max_length=200,null=False, blank=False)
    marca = models.CharField(max_length=255,null=False, blank=False)
    imagen = models.FileField(blank=True,null=True,upload_to=upload_path)
    precioNormal = models.FloatField(null=False, blank=False)
    precioSupermonedas = models.CharField(max_length=200,null=False, blank=False)
    efectivo = models.FloatField(null=False, blank=False)
    codigoQR = models.CharField(max_length=200,null=True, blank=True)
    cantidad = models.IntegerField(null=False, blank=False)
    empresa_id = models.CharField(max_length=200, null=False, blank=False)
    tipo = models.CharField(max_length=255,null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)