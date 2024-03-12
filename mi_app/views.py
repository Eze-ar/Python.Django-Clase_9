from .models import Usuario
from django.shortcuts import render

def crear_usuario(request):
    usuario = Usuario.objects.create(nombre = 'Aldo', email = 'aldo@mail.com')
    return render(request, 'usuarios.html', {'usuarios' : usuario})
