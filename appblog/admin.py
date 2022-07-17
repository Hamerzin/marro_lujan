from django.contrib import admin
from .models import Avatar, Productos, profesor
# Register your models here.
admin.site.register(profesor)
admin.site.register(Productos)
admin.site.register(Avatar)
