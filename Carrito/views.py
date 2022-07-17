from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from Carrito.Carrito import Carrito
from Carrito.models import CarritoModel


def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = CarritoModel.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = CarritoModel.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = CarritoModel.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = CarritoModel.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

