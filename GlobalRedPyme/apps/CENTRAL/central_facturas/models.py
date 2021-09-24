from djongo import models

def upload_path(instance, filname):
    return '/'.join(['CENTRAL/imgFacturas', filname])

def upload_path2(instance, filname):
    return '/'.join(['CENTRAL/archivosFacturas', filname])

# Create your models here.
class Facturas(models.Model):
    _id = models.ObjectIdField()
    numeroFactura = models.CharField(max_length=200,null=False, blank=False)
    razonSocial = models.TextField(max_length=200,null=False, blank=False)
    provincia = models.CharField(max_length=255,null=True, blank=True)
    ciudad = models.CharField(max_length=255,null=True, blank=True)
    fechaEmision = models.DateField(null=False, blank=False)
    importeTotal = models.FloatField(null=False, blank=False)
    categoria = models.CharField(max_length=200,null=True, blank=True)
    urlFoto = models.FileField(blank=True,null=True,upload_to=upload_path)
    urlArchivo = models.FileField(blank=True,null=True,upload_to=upload_path2)
    estado = models.CharField(max_length=200,null=True, blank=True, default='Sin calificar')    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

class CalificarCompras(models.Model):
    _id = models.ObjectIdField()
    atencion = models.CharField(max_length=255,null=True, blank=True)
    calificacion = models.SmallIntegerField(null=True, blank=True)
    observaciones = models.TextField(max_length=200,null=False, blank=False)
    factura = models.ForeignKey(Facturas, related_name='calificaciones', null=True, blank=True, on_delete=models.DO_NOTHING)  # Relacion Calificar Facturas

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)




