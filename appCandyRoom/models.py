from django.db import models

class Stock(models.Model): 
    producto = models.CharField(max_length = 50)
    cantidad = models.IntegerField()
    precio = models.FloatField()

class Proveedores(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField()

class Ventas(models.Model):
    cliente = models.CharField(max_length = 50)
    total = models.FloatField()
    madio_de_pago = models.CharField(max_length = 50)

class Gastos_Generales(models.Model):
    especificacion = models.CharField(max_length = 50)
    monto = models.FloatField() 
