from django.urls import path
from appCandyRoom.views import * 

urlpatterns = [
    path('', inicio),
    path('stock/', stock, name='stock'), 
    path('proveedores/', proveedores, name='proveedores'), 
    path('ventas/', ventas, name='ventas'), 
    path('gastos/', gastos_generales, name='gastos'),
]

