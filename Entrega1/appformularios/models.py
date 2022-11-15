from django.db import models

# Create your models here.

#Aqui creo las clases para la base de datos
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=25)
    email = models.EmailField()
    sector = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(max_length=20)
    familia = models.CharField(max_length=40)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    colonia = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()