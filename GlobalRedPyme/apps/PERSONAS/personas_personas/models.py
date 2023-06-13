import jsonfield
from djongo import models

clave_secreta = b'gldykjM7qTdjud6MHidFotaeepo_3hbdFmnLruYjrxY='

def upload_path(instance, filname):
    return '/'.join(['PERSONAS/imgPersonas', str(instance._id) + "_" + filname])


# Create your models here.
class Personas(models.Model):
    _id = models.ObjectIdField()
    identificacion = models.TextField()
    nombres = models.TextField()
    apellidos = models.TextField()
    nombresCompleto = models.TextField()
    genero = models.TextField()
    fechaNacimiento = models.TextField()
    edad = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    direccion = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    emailAdicional = models.CharField(max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=150, null=True, blank=True)
    facebook = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    twitter = models.CharField(max_length=250, blank=True, null=True)
    tiktok = models.CharField(max_length=250, blank=True, null=True)
    youtube = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.FileField(blank=True, null=True, upload_to=upload_path)
    user_id = models.CharField(max_length=250, blank=False, null=False)  # Relacion usuario
    nivelInstruccion = models.TextField()
    tipoVivienda = models.TextField()
    nombreDueno = models.TextField()
    direccionDomicilio = models.TextField()
    referenciaDomicilio = models.TextField()
    ocupacionSolicitante = models.TextField()
    referenciasSolicitante = models.TextField()
    ingresosSolicitante = models.TextField()
    gastosSolicitante = models.TextField()
    estadoCivil = models.TextField()
    tipoIdentificacion = models.TextField()
    tipoPersona = models.TextField()
    celular = models.TextField()
    codigoUsuario = models.TextField()
    autorizacion = models.TextField()
    garante = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


class ValidarCuenta(models.Model):
    _id = models.ObjectIdField()
    codigo = models.CharField(max_length=200, null=False)
    user_id = models.CharField(max_length=250, blank=False, null=False)  # Relacion usuario

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
