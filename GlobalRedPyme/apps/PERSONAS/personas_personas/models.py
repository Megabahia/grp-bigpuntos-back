from djongo import models

def upload_path(instance, filname):
    return '/'.join(['PERSONAS/imgPersonas', str(instance._id) + "_" + filname])

# Create your models here.
class Personas(models.Model):
    _id = models.ObjectIdField()
    identificacion = models.CharField(max_length=200,null=True)
    nombres = models.CharField(max_length=200,null=True)
    apellidos = models.CharField(max_length=200,null=True)
    genero = models.CharField(max_length=200,null=True)
    fechaNacimiento = models.DateField(null=True)
    edad = models.SmallIntegerField(null=True)
    ciudad = models.CharField(max_length=200,null=True)
    provincia = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=250,blank=True, null=True)
    emailAdicional = models.CharField(max_length=250,blank=True, null=True)
    whatsapp = models.CharField(max_length=150,null=True)
    facebook = models.CharField(max_length=250,blank=True, null=True)
    instagram = models.CharField(max_length=250,blank=True, null=True)
    twitter = models.CharField(max_length=250,blank=True, null=True)
    tiktok = models.CharField(max_length=250,blank=True, null=True)
    youtube = models.CharField(max_length=250,blank=True, null=True)
    imagen = models.FileField(blank=True,null=True,upload_to=upload_path)
    user_id = models.CharField(max_length=250,blank=False, null=False)  # Relacion usuario
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


class ValidarCuenta(models.Model):
    _id = models.ObjectIdField()
    codigo = models.CharField(max_length=200,null=False)
    user_id = models.CharField(max_length=250,blank=False, null=False)  # Relacion usuario

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)