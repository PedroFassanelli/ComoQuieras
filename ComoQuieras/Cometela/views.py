from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
# Create your views here.

from Cometela.models import Vianda, Tamaño, ViandaTamaño
from Cometela.carrito import Carrito
from Cometela.forms import FormCargaVianda, FormCargaSemana
from pedidos.models import Pedido

from django.http import JsonResponse


#Necesitas estar logueado para acceder a la tienda
@login_required(login_url="/autenticacion/iniciar_sesion")
def tienda(request):
    #Si el usuario logueado es de RRHH, no accede a la tienda sino que al panel de rrhh
    if (es_rrhh(request.user)):
        return rrhh(request)
    
    #TODO deberiamos contemplar que el usuario pueda modificar su pedido¿?
    #Si el usuario ya tiene un pedido activo, no puede realizar otro
    if (tiene_pedido_activo(request.user)):
        return render(request, "pedido_realizado.html")
    
    #Si no existen viandas activas
    if (existen_viandas_activas() == False):
        return render(request, "fuera_de_termino.html")

    viandas = Vianda.objects.filter(estado='ACTIVA')
    tamaños = Tamaño.objects.filter(estado='ACTIVA')
    viandas_tamaños = ViandaTamaño.objects.all()
    viandas_tamaños_activas = []
    for x in viandas_tamaños:
        if x.vianda.estado == 'ACTIVA':
            viandas_tamaños_activas.append(x)
    
    dias = ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES']

    return render(request, "viandas.html", {'viandas': viandas, 'tamaños': tamaños, 'viandas_tamaños': viandas_tamaños_activas, 'dias':dias})

#Control de que el usuario ya tenga un pedido activo
def tiene_pedido_activo(user):
    pedidos = Pedido.objects.filter(user=user).filter(estado='ACTIVO')
    if len(pedidos) == 1:
        return True
    return False

#Si no existen viandas activas
def existen_viandas_activas():
    viandas_activas = Vianda.objects.filter(estado='ACTIVA')
    if len(viandas_activas) > 0:
        return True
    return False



### MANEJO DE CARRITO ###

def agregar_vianda(request, vianda_tamaño_id):
    carrito = Carrito(request)
    vianda_tamaño = ViandaTamaño.objects.get(id=vianda_tamaño_id)
    carrito.agregar(vianda_tamaño)
    
    return redirect("Tienda")

#Agregar y Restar viandas con Peticiones AJAX
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def ajax_agregar_vianda(request):
    if is_ajax(request=request) and request.method =="GET":
        vianda_tamaño_id = request.GET.get("vianda_tamaño_id")
        carrito = Carrito(request)
        vianda_tamaño = ViandaTamaño.objects.get(id=vianda_tamaño_id)
        carrito.agregar(vianda_tamaño)

    return JsonResponse({'context': 'True'}, status = 200)

def ajax_restar_vianda(request):
    if is_ajax(request=request) and request.method =="GET":
        vianda_tamaño_id = request.GET.get("vianda_tamaño_id")
        carrito = Carrito(request)
        vianda_tamaño = ViandaTamaño.objects.get(id=vianda_tamaño_id)
        carrito.restar(vianda_tamaño)

    return JsonResponse({'valid': 'True'}, status = 200)

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

#Cargar una vianda para probar (SACAR)
def cargar_vianda(request):

    if request.method == "POST":

        form = FormCargaVianda(request.POST)
    
        if form.is_valid():
            nueva_vianda = form.save(commit=False)
            Vianda.objects.create(
                estado = 'ACTIVA',
                dia = nueva_vianda.dia,
                fecha = nueva_vianda.fecha,
                descripcion = nueva_vianda.descripcion,
                tipo = nueva_vianda.tipo,
            )
    else:
        form = FormCargaVianda()

    return render(request, 'create.html', {"form": form})


### PARTE DE RRHH ###

#Control de que el usuario pertenezca al grupo RRHH
def es_rrhh(user):
    return user.groups.filter(name__in=['RRHH'])

#Vista RRHH
@user_passes_test(es_rrhh)
def rrhh(request):
    viandas_activas = Vianda.objects.filter(estado='ACTIVA')
    permite_carga = True
    if len(viandas_activas)>0:
            permite_carga = False

    return render(request, "rrhh_inicio.html", {'permite_carga': permite_carga, 'viandas':viandas_activas})

#Cargar las viandas de la semana
@user_passes_test(es_rrhh)
def cargar_semana(request):
    
    if request.method == "POST":

        form = FormCargaSemana(request.POST)

        if form.is_valid():
            tamaño1 = Tamaño()
            tamaño2 = Tamaño()
            vianda1 = Vianda()
            vianda2 = Vianda()
            vianda3 = Vianda()
            vianda4 = Vianda()
            vianda5 = Vianda()
            vianda6 = Vianda()
            vianda7 = Vianda()
            vianda8 = Vianda()
            vianda9 = Vianda()
            vianda10 = Vianda()
            vianda11 = Vianda()
            vianda12 = Vianda()
            vianda13 = Vianda()
            vianda14 = Vianda()
            vianda15 = Vianda()
            
            #PRECIOS
            tamaño1.tamaño = 'MEDIA'
            tamaño1.precio = request.POST["precio_media"]
            tamaño1.estado = 'ACTIVA'
            tamaño1.save()
            tamaño2.tamaño = 'ENTERA'
            tamaño2.precio = request.POST["precio_entera"]
            tamaño2.estado = 'ACTIVA'
            tamaño2.save()

            #LUNES
            vianda1.estado='ACTIVA'
            vianda1.dia = 'LUNES'
            vianda1.fecha = request.POST["fecha1"]
            vianda1.descripcion = request.POST["menu1"]
            vianda1.tipo = 'TRADICIONAL'
            vianda1.save()

            vianda2.estado='ACTIVA'
            vianda2.dia = 'LUNES'
            vianda2.fecha = request.POST["fecha1"]
            vianda2.descripcion = request.POST["menu2"]
            vianda2.tipo = 'LIGHT'
            vianda2.save()

            vianda3.estado='ACTIVA'
            vianda3.dia = 'LUNES'
            vianda3.fecha = request.POST["fecha1"]
            vianda3.descripcion = request.POST["menu3"]
            vianda3.tipo = 'VEGGIE'
            vianda3.save()

            #MARTES
            vianda4.estado='ACTIVA'
            vianda4.dia = 'MARTES'
            vianda4.fecha = request.POST["fecha2"]
            vianda4.descripcion = request.POST["menu4"]
            vianda4.tipo = 'TRADICIONAL'
            vianda4.save()

            vianda5.estado='ACTIVA'
            vianda5.dia = 'MARTES'
            vianda5.fecha = request.POST["fecha2"]
            vianda5.descripcion = request.POST["menu5"]
            vianda5.tipo = 'LIGHT'
            vianda5.save()

            vianda6.estado='ACTIVA'
            vianda6.dia = 'MARTES'
            vianda6.fecha = request.POST["fecha2"]
            vianda6.descripcion = request.POST["menu6"]
            vianda6.tipo = 'VEGGIE'
            vianda6.save()

            #MIERCOLES
            vianda7.estado='ACTIVA'
            vianda7.dia = 'MIERCOLES'
            vianda7.fecha = request.POST["fecha3"]
            vianda7.descripcion = request.POST["menu7"]
            vianda7.tipo = 'TRADICIONAL'
            vianda7.save()

            vianda8.estado='ACTIVA'
            vianda8.dia = 'MIERCOLES'
            vianda8.fecha = request.POST["fecha3"]
            vianda8.descripcion = request.POST["menu8"]
            vianda8.tipo = 'LIGHT'
            vianda8.save()

            vianda9.estado='ACTIVA'
            vianda9.dia = 'MIERCOLES'
            vianda9.fecha = request.POST["fecha3"]
            vianda9.descripcion = request.POST["menu9"]
            vianda9.tipo = 'VEGGIE'
            vianda9.save()

            #JUEVES
            vianda10.estado='ACTIVA'
            vianda10.dia = 'JUEVES'
            vianda10.fecha = request.POST["fecha4"]
            vianda10.descripcion = request.POST["menu10"]
            vianda10.tipo = 'TRADICIONAL'
            vianda10.save()

            vianda11.estado='ACTIVA'
            vianda11.dia = 'JUEVES'
            vianda11.fecha = request.POST["fecha4"]
            vianda11.descripcion = request.POST["menu11"]
            vianda11.tipo = 'LIGHT'
            vianda11.save()

            vianda12.estado='ACTIVA'
            vianda12.dia = 'JUEVES'
            vianda12.fecha = request.POST["fecha4"]
            vianda12.descripcion = request.POST["menu12"]
            vianda12.tipo = 'VEGGIE'
            vianda12.save()

            #VIERNES
            vianda13.estado='ACTIVA'
            vianda13.dia = 'VIERNES'
            vianda13.fecha = request.POST["fecha5"]
            vianda13.descripcion = request.POST["menu13"]
            vianda13.tipo = 'TRADICIONAL'
            vianda13.save()

            vianda14.estado='ACTIVA'
            vianda14.dia = 'VIERNES'
            vianda14.fecha = request.POST["fecha5"]
            vianda14.descripcion = request.POST["menu14"]
            vianda14.tipo = 'LIGHT'
            vianda14.save()

            vianda15.estado='ACTIVA'
            vianda15.dia = 'VIERNES'
            vianda15.fecha = request.POST["fecha5"]
            vianda15.descripcion = request.POST["menu15"]
            vianda15.tipo = 'VEGGIE'
            vianda15.save()
            

            return redirect('Recursos Humanos')

    else:
        form = FormCargaSemana()
    
    return render(request, 'cargar_semana.html', {"form": form})

#TODO Ver como editar semana - Mejora a futuro, podemos modificar desde admin.
#Actualmente no se usa
def editar_semana(request):
    context = {}

    semana = Vianda.objects.filter(estado = 'ACTIVA')

    context['instance'] = semana

    if request.method == 'POST':
        form = FormCargaSemana(request.POST, instance=semana)
        if form.is_valid():
            form.save()
            return redirect('Tienda')
    else:
        form = FormCargaSemana(instance=semana)
    context['form'] = form
    return render(request, 'cargar_semana.html', context=context)


#ESTO HABRÍA QUE LLAMARLO LUEGO DE GENERAR EL REPORTE
@user_passes_test(es_rrhh)
def desactivar_viandas(request):

    viandas = Vianda.objects.filter(estado='ACTIVA')
    tamaños = Tamaño.objects.filter(estado='ACTIVA')
    pedidos = Pedido.objects.filter(estado='ACTIVO')
    for vianda in viandas:
        vianda.estado = 'INACTIVA'
        vianda.save()
    for tamaño in tamaños:
        tamaño.estado = 'INACTIVA'
        tamaño.save()
    for pedido in pedidos:
        pedido.estado = 'INACTIVO'
        pedido.save()

    return redirect(rrhh)
