from djongo import models

def upload_path(instance, filname):
    return '/'.join(['CENTRAL/imgPublicaciones', str(instance._id) + "_" + filname])

# Create your models here.
class Publicaciones(models.Model):
    _id = models.ObjectIdField()
    titulo = models.CharField(max_length=200,null=False)
    subtitulo = models.CharField(max_length=200,null=False)
    descripcion = models.TextField(null=False)
    imagen = models.ImageField(blank=True,null=True,upload_to=upload_path)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
