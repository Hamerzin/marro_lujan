from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView
from django.views import View
from appblog import views
from appblog.views import *

urlpatterns = [

path('curso/list', views.ProfesorList.as_view(), name='list'),
path('', views.index, name="index"),
path('index', views.index, name="index"),
path(r'^(?P<pk>\d+)$', views.ProfesorDetalle.as_view(), name='Detalle'),
path(r'^nuevo$', views.ProfesorCreacion.as_view(), name='New'),
path(r'^editar/(?P<pk>\d+)$', views.ProfesorEditar.as_view(), name='Editar'),


path('login', views.login_request, name='login'),
path('register', views.register, name="register"),
path('logout',views.logout_request, name='logout' ),
path('logout2', LogoutView.as_view(template_name='index.html'), name = 'logout2'),
path('editar',views.editarPerfil, name='editar' ),
path ('enviarCorreo', views.enviarCorreo, name='enviarCorreo'),
]