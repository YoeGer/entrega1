from django.shortcuts import render
from appCandyRoom.forms import *
from .models import *

def inicio(request): 
    return render (request, "appCandyRoom/inicio.html")

def stock(request): 
    return render (request, "appCandyRoom/stock.html")

def proveedores(request): 
    return render (request, "appCandyRoom/proveedores.html")

def ventas(request): 
    return render (request, "appCandyRoom/ventas.html")

def gastos_generales(request): 
    return render (request, "appCandyRoom/gastos.html")

def stock (request): 
    if request.method == "POST": 
        form = StockForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            producto_en_stock = Stock(producto= informacion['producto'], cantidad= informacion ['cantidad'], precio= informacion['precio'])
            producto_en_stock.save()
            return render (request, "appCandyRoom/inicio.html", {'mensaje' : 'Producto cargado '})
    else:
        form = StockForm()
    return render (request, "appCandyRoom/stock.html", {'form': form})

def proveedores (request): 
    if request.method == "POST": 
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            proveedor = Proveedores(nombre= informacion['nombre'], apellido= informacion ['apellido'], email= informacion['email'])
            proveedor.save()
            return render (request, "appCandyRoom/inicio.html", {'mensaje' : 'Proveedor cargado '})
    else:
        form = ProveedoresForm()
    return render (request, "appCandyRoom/proveedores.html", {'form': form})     

def ventas (request): 
    if request.method == "POST": 
        form = VentasForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            venta = Ventas(cliente= informacion['cliente'], total= informacion ['total'], medio_de_pago= informacion['medio_de_pago'])
            venta.save()
            return render (request, "appCandyRoom/inicio.html", {'mensaje' : 'Venta cargada '})
    else:
        form = VentasForm()
    return render (request, "appCandyRoom/ventas.html", {'form': form})   

def gastos_generales (request): 
    if request.method == "POST": 
        form = Gastos_GeneralesForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            gasto = Gastos_Generales(especificacion= informacion['especificacion'], monto= informacion ['monto'])
            gasto.save()
            return render (request, "appCandyRoom/inicio.html", {'mensaje' : 'Gasto cargado '})
    else:
        form = Gastos_GeneralesForm()
    return render (request, "appCandyRoom/gastos.html", {'form': form})   