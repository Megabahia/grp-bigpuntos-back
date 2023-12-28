from djongo import models
from django.utils import timezone


def upload_path(instance, filname):
    """
    Este metodo se utiliza para subir los archivos
    @type filname: el campo filname es el nombre del archivo
    @type instance: el campo instance es el registro que se esta guardando
    @rtype: Devuelve la ruta del archivo donde se guardo
    """
    return '/'.join(['CORP/documentosCreditosArchivos', str(timezone.localtime(timezone.now())) + "_" + filname])


# Mundo: bigpuntos
# Portales: PERSONAS, coop, center
# Esta clase sirve para conectar con la tabla PreAprobados de la base datos corp
class PreAprobados(models.Model):
    fechaCargaArchivo = models.DateField(null=True)
    campania = models.CharField(max_length=255, null=True, blank=True)
    registrosCargados = models.CharField(max_length=255, null=True, blank=True)
    linkArchivo = models.FileField(blank=True, null=True, upload_to=upload_path)
    tamanioArchivo = models.CharField(max_length=255, null=True, blank=True)
    usuarioCargo = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)  # Relacion de usuario
    tipoCredito = models.CharField(max_length=255, null=True, blank=True)
    empresa_financiera = models.CharField(max_length=255, null=True, blank=True)
    empresa_comercial = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True, default='Pendiente Carga')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

def upload_path_comisiones(instance, filname):
    """
    Este metodo se utiliza para subir los archivos
    @type filname: el campo filname es el nombre del archivo
    @type instance: el campo instance es el registro que se esta guardando
    @rtype: Devuelve la ruta del archivo donde se guardo
    """
    return '/'.join(['CORP/documentosComisionesArchivos', str(timezone.localtime(timezone.now())) + "_" + filname])


# Mundo: bigpuntos
# Portales: PERSONAS, coop, center
# Esta clase sirve para conectar con la tabla PreAprobados de la base datos corp
class ArchivosComisiones(models.Model):
    _id = models.ObjectIdField()
    fechaCargaArchivo = models.DateField(null=True)
    campania = models.CharField(max_length=255, null=True, blank=True)
    registrosCargados = models.CharField(max_length=255, null=True, blank=True)
    linkArchivo = models.FileField(blank=True, null=True, upload_to=upload_path_comisiones)
    tamanioArchivo = models.CharField(max_length=255, null=True, blank=True)
    usuarioCargo = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    tipoArchivo = models.CharField(max_length=255, null=True, blank=True)
    empresa_financiera = models.CharField(max_length=255, null=True, blank=True)
    empresa_comercial = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True, default='Pendiente Carga')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
