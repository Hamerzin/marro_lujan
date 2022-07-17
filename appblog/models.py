from ast import Return
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from django.template.defaultfilters import slugify

class profesor(models.Model):
    clase=models.CharField(max_length=50)
    camada=models.IntegerField()
    
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)
    
class Productos(models.Model):
    
    tipo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    precio=models.IntegerField()

