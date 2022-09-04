from django import forms 

class StockForm (forms.Form):
    producto = forms.CharField(max_length = 50)
    cantidad = forms.IntegerField()
    precio = forms.FloatField()

class ProveedoresForm (forms.Form):
    nombre = forms.CharField(max_length = 50)
    apellido = forms.CharField(max_length = 50)
    email = forms.EmailField()

class VentasForm(forms.Form):
    cliente = forms.CharField(max_length = 50)
    total = forms.FloatField()
    medio_de_pago = forms.CharField(max_length = 50)

class Gastos_GeneralesForm(forms.Form):
    especificacion = forms.CharField(max_length = 50)
    monto = forms.FloatField() 