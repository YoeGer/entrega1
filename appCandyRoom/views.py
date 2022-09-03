from django.shortcuts import render

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

