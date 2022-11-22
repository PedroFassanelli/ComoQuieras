from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from Cometela.carrito import Carrito
from pedidos.models import Pedido, LineaPedido
from ComoQuieras.urls import tienda
# Create your views here.

#Cuando el usuario hace click en "Enviar Pedido"
@login_required(login_url="/autenticacion/login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carrito = Carrito(request)
    lineas_pedido = list()
    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(
            vianda_tamaño_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    #Inserta en la BD
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )

    messages.success(request, "El pedido se ha realizado correctamente!")

    return redirect(tienda)

def enviar_mail(**kwargs):

    asunto="PEDIDO DE VIANDAS SEMANAL"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario"),

    })

    mensaje_texto = strip_tags(mensaje)
    #Ver este email
    from_email="viandaswiltel@gmail.com"
    to=kwargs.get("email_usuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)