from django.db import models

# Create your models here.

class Categorias(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100)
  estado = models.BooleanField(default=True, null=True)


class Productos(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=200, null=False)
  descripcion = models.CharField(max_length=200, null=False)
  precio = models.DecimalField(max_digits=5, decimal_places=2)
  estado = models.BooleanField(default=True, null=True)
