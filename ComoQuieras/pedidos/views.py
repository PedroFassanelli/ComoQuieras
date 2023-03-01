from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


from Cometela.carrito import Carrito
from Cometela.models import ViandaTamaño, Vianda
from pedidos.models import Pedido, LineaPedido
from ComoQuieras.urls import tienda


# Create your views here.

#Cuando el usuario hace click en "Enviar Pedido" 
def procesar_pedido(request):
    #Chequeo si ya existe un pedido activo del usuario
    pedido_activo = Pedido.objects.filter(user=request.user, estado='ACTIVO')
    if len(pedido_activo) == 1:
        messages.success(request, "Ya realizaste el pedido semanal!")
    else:
        carrito = Carrito(request)
        #Controlo que el carrito no esté vacío antes de crear el pedido
        if carrito.carrito.items():
            pedido = Pedido.objects.create(user=request.user, estado ='ACTIVO')
            lineas_pedido = list()
            for key, value in carrito.carrito.items():
                lineas_pedido.append(LineaPedido(
                    vianda_tamaño_id = key,
                    cantidad = value["cantidad"],
                    user = request.user,
                    pedido = pedido
                ))
                pedido.total = pedido.total + value["acumulado"]
                pedido.save()
                
            #Inserta en la BD
            LineaPedido.objects.bulk_create(lineas_pedido)

            enviar_mail(
                pedido=pedido,
                lineas_pedido=lineas_pedido,
                nombre_usuario=request.user.first_name,
                email_usuario=request.user.email
            )

            #messages.success(request, "El pedido se ha realizado correctamente!")

    return redirect('CLS')

def enviar_mail(**kwargs):

    asunto="PEDIDO DE VIANDAS SEMANAL"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario"),
    })

    mensaje_texto = strip_tags(mensaje)
    #Ver de cambiar este email
    from_email="viandaswiltel@gmail.com"
    to=kwargs.get("email_usuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

#Listar Historial de pedidos realizado por un usuario
def mostrar_pedidos(request):
    pedidos = Pedido.objects.order_by('-created_at').filter(user = request.user)
    lineas_pedidos = LineaPedido.objects.filter(user = request.user)

    return render(request, 'historial.html', {'lista_pedidos': pedidos, 'lista_lineas_pedidos': lineas_pedidos})

#Listar pedidos ACTIVOS realizados por todos los usuarios, para RRHH
def mostrar_pedidos_rrhh(request):
    pedidos = Pedido.objects.order_by('-created_at').filter(estado='ACTIVO')
    lineas_pedidos = LineaPedido.objects.all()
    
    return render(request, 'pedidos_activos.html', {'lista_pedidos': pedidos, 'lista_lineas_pedidos': lineas_pedidos})


