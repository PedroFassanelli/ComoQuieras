from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from ComoQuieras.urls import tienda
# Create your views here.

def cerrar_sesion(request):
    logout(request)

    return redirect(tienda)

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect(tienda)
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")


    form = AuthenticationForm()

    return render(request, "login/login.html", {"form":form})