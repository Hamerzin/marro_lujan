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
import smtplib
# Create your views here.



class ProfesorList(LoginRequiredMixin, ListView):
    model=profesor
    template_name="profesor_list.html"

class ProfesorDetalle(DetailView):
    model=profesor
    template_name="profesor_detalle.html"
    
def logout_request(request):
      logout(request)
     
      return redirect("Login")

    


class ProfesorCreacion(CreateView):
    model=profesor
    template_name="profesor_create.html"
    fields=['clase','camada']
    success_url=reverse_lazy('list')

class ProfesorEditar(UpdateView):
    model=profesor
    template_name="profesor_form.html"
    fields=['clase','camada']
    success_url=reverse_lazy('list')

class ProfesorDelete(DeleteView):
    model=profesor
    template_name="profesor_confirm_delete.html"
    success_url=reverse_lazy('list')

#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return render (request, "index.html",{'url': buscar_url_avatar(request.user.id)})
                  else:
                        print(2)
                        return render (request, "index.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "login2.html", {'form': form,"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
      print(3)
      return render(request, "login2.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "registro.html", {"form": form})



@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']
                 
                  usuario.save()
            
                  return render(request, "inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name})
      
      #voy al HTML que me permite editar
      return render(request, "editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario,'url': buscar_url_avatar(request.user.id)})

@login_required
def indexpage(request):
      return render(request,"inicio.html")

def index(request):
      if request.user.is_authenticated:
            #avatares=Avatar.objects.filter(user=request.user.id)
            return render(request, "index.html",{'url': buscar_url_avatar(request.user.id)})
      else:
            return render(request, "index.html" )

def buscar_url_avatar(user):
    avatares = Avatar.objects.filter(user=user)
    if avatares.exists():
        # Se usa first() para obtener el primer objeto
        return avatares.first().imagen.url

    # Si no existe el avatar regresar un None
    return None



def enviarCorreo(request):
    try:

        mensaje = request.GET.get('mensaje')
        correo_electronico = request.GET.get('correo')
        asunto = request.GET.get('asunto')

        body = 'Subject: {}\n\n{}'.format(asunto, mensaje)
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login('jamerdipa@gmail.com','Natu-190')
        server.sendmail('jamerdipa@gmail.com', correo_electronico, body)
        server.quit()
        return JsonResponse({'status':True, 'mensaje':'Correo enviado exitosamente'})

    except Exception as e:
        return JsonResponse({'status':False, 'mensaje':'Ocurrio un error al momento de enviar el correo', 'error':e.__str__()})