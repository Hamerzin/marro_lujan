from django.shortcuts import render
from appblog.views import buscar_url_avatar

# Create your views here.
def sobrenos(request):
    return render(request, "sobre_nosotros.html",{'url': buscar_url_avatar(request.user.id)})
