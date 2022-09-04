from django.db import models

class Stock(models.Model): 
    producto = models.CharField(max_length = 50)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    def __str__(self): 
        return self.producto + " " + str(self.cantidad)

class Proveedores(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField()

    def __str__(self): 
        return self.nombre + " " + self.apellido + " " + self.email

class Ventas(models.Model):
    cliente = models.CharField(max_length = 50)
    total = models.FloatField()
    medio_de_pago = models.CharField(max_length = 50)

    def __str__(self): 
        return self.cliente + " " + "$"+str(self.total)

class Gastos_Generales(models.Model):
    especificacion = models.CharField(max_length = 50)
    monto = models.FloatField() 

    def __str__(self): 
        return self.especificacion + " " + "$"+str(self.monto)