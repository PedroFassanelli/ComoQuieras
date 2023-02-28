"""ComoQuieras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Cometela.carrito import Carrito
from Cometela.views import tienda, agregar_vianda, eliminar_vianda, restar_vianda, limpiar_carrito, cargar_vianda, cargar_semana, desactivar_viandas, rrhh, editar_semana

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tienda, name = "Tienda"),
    path('agregar/<int:vianda_tamaño_id>/', agregar_vianda, name="Add"),
    path('eliminar/<int:vianda_tamaño_id>/', eliminar_vianda, name="Del"),
    path('restar/<int:vianda_tamaño_id>/', restar_vianda, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    #path('cargar/', cargar_vianda, name="Cargar"),
    path('cargar_semana/', cargar_semana, name="Cargar Semana"),
    path('editar_semana/', editar_semana, name="Editar Semana"),
    path('desactivar_viandas/', desactivar_viandas, name="Desactivar Viandas"),
    path('rrhh/', rrhh, name="Recursos Humanos"),

    path('autenticacion/', include('autenticacion.urls')),

    path('pedidos/', include('pedidos.urls')),

    path('reports/', include('reports.urls')),

]
