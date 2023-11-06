from django.db import models


# Mundo: Bigpuntos
#Portales: Corp
#Esta clase sirve para relacionar con la tabla prediccion de la base datos mdo
class PrediccionCrosseling(models.Model):
    factura_id = models.PositiveIntegerField(null=False)
    # codigo = models.AutoField(null=False)
    fechaPredicciones = models.DateField(null=True)
    nombres = models.CharField(max_length=255, null=False)
    apellidos = models.CharField(max_length=255, null=False)
    identificacion = models.CharField(max_length=13, null=False)
    telefono = models.CharField(max_length=250, null=True)
    correo = models.EmailField(max_length=255, null=True)
    cliente = models.SmallIntegerField(null=True)
    negocio = models.SmallIntegerField(null=True)
    total = models.FloatField(null=True)
    # Id de la empresa que se inicia sesion
    empresa_id = models.CharField(max_length=255, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


# Mundo: Bigpuntos
#Portales: Corp
#Esta clase sirve para relacionar con la tabla prediccion detalles de la base datos mdo
class Detalles(models.Model):
    prediccionCrosseling = models.ForeignKey(PrediccionCrosseling, related_name='detalles', null=True, blank=True,
                                             on_delete=models.DO_NOTHING)  # Relacion Factura
    articulo = models.CharField(max_length=150, null=True)
    valorUnitario = models.FloatField(null=True)
    cantidad = models.PositiveIntegerField(null=True)
    precio = models.FloatField(null=True)
    codigo = models.CharField(max_length=250, null=True)
    informacionAdicional = models.TextField(null=True)
    descuento = models.FloatField(null=True)
    impuesto = models.FloatField(null=True)
    valorDescuento = models.FloatField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
