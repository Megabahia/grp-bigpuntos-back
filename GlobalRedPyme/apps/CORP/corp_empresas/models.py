from djongo import models


def upload_path(instance, filname):
    return '/'.join(['CORP/imgEmpresas', str(instance._id) + "_" + filname])


# Create your models here.
class Empresas(models.Model):
    _id = models.ObjectIdField()
    ruc = models.CharField(max_length=13, null=True, blank=True)
    nombreEmpresa = models.TextField(null=True, blank=True)
    nombreComercial = models.TextField(null=True, blank=True)
    tipoEmpresa = models.CharField(max_length=200, null=True, blank=True)
    tipoCategoria = models.CharField(max_length=200, null=True, blank=True)
    pais = models.CharField(max_length=200, null=True, blank=True)
    provincia = models.CharField(max_length=200, null=True, blank=True)
    ciudad = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    telefono1 = models.CharField(max_length=20, null=True, blank=True)
    telefono2 = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(max_length=255, null=True, blank=True)
    estado = models.CharField(default="Activo", max_length=200, null=True, blank=True)
    imagen = models.FileField(blank=True, null=True, upload_to=upload_path)
    numeroCuenta = models.TextField(max_length=255, null=True, blank=True)
    titularCuenta = models.TextField(max_length=255, null=True, blank=True)
    correoTitular = models.EmailField(max_length=255, null=True, blank=True)
    bancoDestino = models.TextField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


class EmpresasConvenio(models.Model):
    _id = models.ObjectIdField()
    empresa = models.CharField(max_length=200, null=True, blank=True)  # Relacion Empresa
    convenio = models.ForeignKey(Empresas, null=False, on_delete=models.CASCADE)  # Relacion Empresas convenio

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


class Empleados(models.Model):
    _id = models.ObjectIdField()
    tipoIdentificacion = models.CharField(max_length=200, null=True, blank=True)
    identificacion = models.CharField(max_length=200, null=True, blank=True)
    nombres = models.CharField(max_length=200, null=True, blank=True)
    apellidos = models.CharField(max_length=200, null=True, blank=True)
    correo = models.EmailField(max_length=200, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    empresa = models.ForeignKey(Empresas, null=False, on_delete=models.CASCADE)  # Relacion Empresas

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
