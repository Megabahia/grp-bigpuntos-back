from djongo import models

def upload_path(instance, filname):
    return '/'.join(['PERSONAS/imgPersonas', str(instance._id) + "_" + filname])

# Create your models here.
class Personas(models.Model):
    _id = models.ObjectIdField()
    identificacion = models.CharField(max_length=200,null=False)
    nombres = models.CharField(max_length=200,null=False)
    apellidos = models.CharField(max_length=200,null=False)
    genero = models.CharField(max_length=200,null=False)
    fechaNacimiento = models.DateField(null=True)
    edad = models.SmallIntegerField(null=True)
    ciudad = models.CharField(max_length=200,null=True)
    provincia = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=250,blank=True, null=True, unique=True)
    emailAdicional = models.CharField(max_length=250,blank=True, null=True, unique=True)
    whatsapp = models.CharField(max_length=150,null=True)
    facebook = models.CharField(max_length=250,blank=True, null=True, unique=True)
    instagram = models.CharField(max_length=250,blank=True, null=True, unique=True)
    twitter = models.CharField(max_length=250,blank=True, null=True, unique=True)
    tiktok = models.CharField(max_length=250,blank=True, null=True, unique=True)
    youtube = models.CharField(max_length=250,blank=True, null=True, unique=True)
    imagen = models.ImageField(blank=True,null=True,upload_to=upload_path)
    user_id = models.CharField(max_length=250,blank=True, null=True, unique=True)  # Relacion usuario
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
