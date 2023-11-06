"""NUBE DE BIGPUNTOS
PORTALES: CENTER, PERSONAS, CORP, IFIS
Este archivo sirve para conectar el backend de la nube de bigpuntos con la base datos de bigpuntos central
"""
from djongo import models

def upload_path(instance, filname):
    """
    Este metodo se utiliza para almacenar las imagenes de la empresa
    @type filname: El campo filename es el nombre del archivo
    @type instance: El campo instance es el registro que se va guardar en la base de datos
    @rtype: REtorna la ruta de donde se guardo la imagen
    """
    return '/'.join(['CENTRAL/imgEmpresas', str(instance._id) + "_" + filname])

# La clase Empresas hace referencia a la tabla de la base de datos de central
class Empresas(models.Model):
    _id = models.ObjectIdField()
    logo = models.FileField(blank=True,null=True,upload_to=upload_path)
    nombre = models.CharField(max_length=200,null=True, blank=True)
    bigPuntos = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255,null=True, blank=True)
    urlClientes = models.CharField(max_length=255,null=True, blank=True)
    type = models.CharField(max_length=255,null=True, blank=True)
    estado = models.CharField(default="Activo",max_length=200,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)