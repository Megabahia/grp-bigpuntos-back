from djongo import models


# Create your models here.
class Empresas(models.Model):
    _id = models.ObjectIdField()
    nombre = models.TextField(null=True, blank=True)
    local = models.TextField(null=True, blank=True)
    provincia = models.CharField(max_length=200,null=True, blank=True)
    ciudad = models.CharField(max_length=200,null=True, blank=True)
    ruc = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=20,null=True, blank=True)
    estado = models.CharField(default="Activo",max_length=200,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)