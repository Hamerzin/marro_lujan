from dataclasses import fields
from distutils.command import upload
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from appblog.models import Productos



    
class FormularioRopa(forms.ModelForm): 
  
    class Meta: 
        model = Productos 
        fields = ['tipo', 'nombre','imagen','precio'] 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    #extendemos el contenido de el formulario viejo agregando dos campos más
    last_name: forms.CharField()
    first_name: forms.CharField()
    
    class Meta:
        model = User                                               #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2','last_name','first_name']
        labels = {'username': 'nombre', 'email':'correo', 'last_name':'apellido', 'first_name':'nombre'}
        help_texts= {k:"" for k in fields}

#La clase meta es una clase interna en los modelos de Django.
#Que contienen opciones Meta (metadatos) que se utilizan para
#cambiar el comportamiento de los campos de su modelo,
#como cambiar las opciones de orden, si el modelo es abstracto o no,
#versiones singulares y plurales del nombre, etc. 

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    #extendemos el contenido de el formulario viejo agregando dos campos más
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','last_name','first_name']
        help_texts= {k:"" for k in fields}


#class models.User
# User objects have the following fields:

# username¶
# Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.

# The max_length should be sufficient for many use cases. If you need a longer length, please use a custom user model. If you use MySQL with the utf8mb4 encoding (recommended for proper Unicode support), specify at most max_length=191 because MySQL can only create unique indexes with 191 characters in that case by default.

# first_name¶
# Optional (blank=True). 150 characters or fewer.

# last_name¶
# Optional (blank=True). 150 characters or fewer.

# email¶
# Optional (blank=True). Email address.

# password¶
# Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the password documentation.

# groups¶
# Many-to-many relationship to Group