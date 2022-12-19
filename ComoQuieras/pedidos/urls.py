from django.urls import path

from .import views

urlpatterns = [
    path('',views.procesar_pedido, name="procesar_pedido"),
    path('historial', views.mostrar_pedidos, name="mostrar_pedidos"),
    path('pedidos_activos', views.mostrar_pedidos_rrhh, name="mostrar_pedidos_activos"),
]