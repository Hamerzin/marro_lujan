from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView
from django.views import View
from productos import views
from productos.views import *

urlpatterns = [
path('productos', views.cargaprod, name='productos'),
path('agregar', views.agregarProducto, name='agregar'),
path('verprods', views.verproductoss,name="verprods"),
path('buscar', views.buscar, name='buscar'),
path ('busqueda', views.buscarprods, name='busqueda'),
path(r'^borrar/(?P<pk>\d+)$', views.ProductosDelete.as_view(), name='Delete'),
path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detalle'),
]