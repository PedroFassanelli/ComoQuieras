from django.contrib import admin
from pedidos.models import Pedido, LineaPedido


admin.site.register([Pedido,LineaPedido])


