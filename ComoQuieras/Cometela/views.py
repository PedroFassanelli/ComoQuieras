from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

from Cometela.models import Vianda
from Cometela.carrito import Carrito


def tienda(request):
    viandas = Vianda.objects.all()

    return render(request, "viandas.html", {'viandas': viandas})

def agregar_vianda(request, vianda_id):
    carrito = Carrito(request)
    vianda = Vianda.objects.get(id=vianda_id)
    carrito.agregar(vianda)
    return redirect("Tienda")

def eliminar_vianda(request, vianda_id):
    carrito = Carrito(request)
    vianda = Vianda.objects.get(id=vianda_id)
    carrito.eliminar(vianda)
    return redirect("Tienda")

def restar_vianda(request, vianda_id):
    carrito = Carrito(request)
    vianda = Vianda.objects.get(id=vianda_id)
    carrito.restar(vianda)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")