from django.urls import path
from appCandyRoom.views import * 

urlpatterns = [
    path('', inicio),
    path('stock/', stock), 
    path('proveedores/', proveedores), 
    path('ventas/', ventas), 
    path('gastos/', gastos_generales)
]