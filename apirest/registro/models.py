from django.db import models

# Create your models here.
class Doctor(models.Model):
    id_doc = models.CharField(blank=False ,max_length=30)
    nombre = models.CharField(max_length=30)
    apellidopa = models.CharField(max_length=30)
    apellidoMa = models.CharField(max_length=30)
    telefono = models.IntegerField(blank=False)
    correo = models.CharField(max_length=30)

class Secretaria(models.Model):
    id_sec = models.CharField(blank=False ,ax_length=30)
    nombre = models.CharField(max_length=30)
    apellidopa = models.CharField(max_length=30)
    apellidoMa = models.CharField(max_length=30)
    telefono = models.IntegerField(blank=False)
    correo = models.CharField(max_length=30)

class Clientes(models.Model):
    id_sec = models.CharField(blank=False, max_length=30)
    nombre = models.CharField(max_length=30)
    apellidopa = models.CharField(max_length=30)
    apellidoMa = models.CharField(max_length=30)
    telefono = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)