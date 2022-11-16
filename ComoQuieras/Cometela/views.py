from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

from Cometela.models import Vianda, Tamaño, ViandaTamaño
from Cometela.carrito import Carrito


def tienda(request):
    viandas = Vianda.objects.all()
    tamaños = Tamaño.objects.all()
    viandas_tamaños = ViandaTamaño.objects.all()

    return render(request, "viandas.html", {'viandas': viandas, 'tamaños': tamaños, 'viandas_tamaños': viandas_tamaños})

def agregar_vianda(request, vianda_tamaño_id):
    carrito = Carrito(request)
    vianda_tamaño = ViandaTamaño.objects.get(id=vianda_tamaño_id)
    carrito.agregar(vianda_tamaño)
    return redirect("Tienda")

def eliminar_vianda(request, vianda_tamaño_id):
    carrito = Carrito(request)
    vianda_tamaño = ViandaTamaño.objects.get(id=vianda_tamaño_id)
    carrito.eliminar(vianda_tamaño)
    return redirect("Tienda")

def restar_vianda(request, vianda_tamaño_id):
    carrito = Carrito(request)
    vianda_tamaño = ViandaTamaño.objects.get(id=vianda_tamaño_id)
    carrito.restar(vianda_tamaño)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")