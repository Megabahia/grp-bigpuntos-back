from djongo import models

def upload_path(instance, filname):
    return '/'.join(['CENTRAL/imgEmpresas', str(instance._id) + "_" + filname])

# Create your models here.
class Empresas(models.Model):
    _id = models.ObjectIdField()
    logo = models.FileField(blank=True,null=True,upload_to=upload_path)
    nombre = models.CharField(max_length=200,null=True, blank=True)
    bigPuntos = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255,null=True, blank=True)
    urlClientes = models.CharField(max_length=255,null=True, blank=True)
    estado = models.CharField(default="Activo",max_length=200,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)