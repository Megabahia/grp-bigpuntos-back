from djongo import models

from apps.CORP.corp_empresas.models import Empresas
from apps.CORP.corp_creditoPreaprobados.models import CreditoPreaprobados

# Create your models here.
class FacturasEncabezados(models.Model):
    numeroFactura = models.CharField(max_length=150,null=True, blank=True)
    fecha = models.DateField(null=True)
    tipoIdentificacion = models.CharField(max_length=150,null=True)
    identificacion = models.CharField(max_length=150,null=True)
    razonSocial = models.CharField(max_length=150,null=True)
    direccion = models.CharField(max_length=150,null=True)
    telefono = models.CharField(max_length=150,null=True)
    correo = models.EmailField(max_length=150,null=True)
    nombreVendedor = models.CharField(max_length=150,null=True)
    subTotal = models.FloatField(null=True)
    descuento = models.FloatField(null=True)
    iva = models.FloatField(null=True)
    total = models.FloatField(null=True)
    canal = models.CharField(max_length=150,null=True)
    numeroProductosComprados = models.IntegerField(null=True)
    user_id = models.CharField(max_length=255,null=True,blank=True) # Relacion de usuario
    empresaComercial = models.ForeignKey(Empresas, null=True, on_delete=models.DO_NOTHING)  # Relacion Con la categoria
    credito = models.ForeignKey(CreditoPreaprobados, null=True, on_delete=models.DO_NOTHING)  # Relacion Con la categoria
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        return super(FacturasEncabezados, self).save(*args, **kwargs)


class FacturasDetalles(models.Model):
    # NOMBRAMOS A LA RELACION DETALLATES
    facturaEncabezado= models.ForeignKey(FacturasEncabezados, related_name='detalles', null=True, blank=True, on_delete=models.DO_NOTHING)  # Relacion Factura
    articulo = models.CharField(max_length=150,null=True)
    valorUnitario = models.FloatField(null=True)
    cantidad = models.PositiveIntegerField(null=True)
    precio = models.FloatField(null=True)
    codigo = models.CharField(max_length=250,null=True)
    informacionAdicional = models.CharField(max_length=250,null=True)
    descuento = models.FloatField(null=True)
    impuesto = models.FloatField(null=True)
    valorDescuento = models.FloatField(null=True)
    total = models.FloatField(null=True)
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        # self.tipo = self.tipo.upper()
        return super(FacturasDetalles, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.id)