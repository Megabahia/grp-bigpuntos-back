from djongo import models


# Create your models here.
class Empresas(models.Model):
    _id = models.ObjectIdField()
    nombre = models.TextField(null=False, blank=False)
    local = models.TextField(null=False, blank=False)
    provincia = models.CharField(max_length=200,null=False, blank=False)
    ciudad = models.CharField(max_length=200,null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)