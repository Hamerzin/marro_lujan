from django.shortcuts import render
from itertools import product
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from appblog import models
from appblog.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from appblog.forms import *
from appblog.views import buscar_url_avatar

# Create your views here.
@login_required
def productos(request):
      return render(request, "inicio.html", {'url': buscar_url_avatar(request.user.id)})
@login_required
def agregarProducto(request):
      if request.method == 'POST':
            
            miFormulario = FormularioRopa(request.POST)
            
            print(miFormulario)
            
            if FormularioRopa.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  
                  ropa = productos(tipo=informacion['tipo'],imagen=informacion['imagen'], nombre=informacion['nombre'],precio=informacion['precio'])                  
                  ropa.save()
                  
                  return render(request, 'inicio.html')
      
      else:
            miFormulario = FormularioRopa()
      
      return render(request, "formulario.html",{"miFormulario":miFormulario})

def cargaprod(request): 
  
    if request.method == 'POST': 
        form = FormularioRopa(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect('verprods')
    else: 
        form = FormularioRopa() 
    return render(request, 'formulario.html', {'form' : form}) 
  
  
def success(request): 
    return render (request,'index.html')

def verproductoss(request): 
      prods = Productos.objects.all()

      return render (request, 'vistaproductos.html', {'prods':prods, 'url': buscar_url_avatar(request.user.id)})

class ProductosDelete(DeleteView):
    model=Productos
    template_name="profesor_confirm_delete.html"
    success_url=reverse_lazy('verprods')
    
class ProductoDetalle(DetailView):
      model=Productos
      template_name="productos_detalle.html"
    
def buscar(request):
      if request.GET['nombre']:
            nombre = request.GET['nombre']

            prods = Productos.objects.filter(nombre__icontains=nombre)
            return render(request, "resultadosBusqueda.html", {"prods": prods, "nombre":nombre, 'url': buscar_url_avatar(request.user.id)} )
           
                  
      else:
            output = "No ingresaste ningun dato"
      
      return HttpResponse(output)

def buscarprods(request):
      return render(request, 'buscarprods.html', {'url': buscar_url_avatar(request.user.id)})