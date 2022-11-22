from django.db import models

from django.contrib.auth import get_user_model
from Cometela.models import ViandaTamaño

from django.db.models import F, Sum, FloatField
# Create your models here.

User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            #Seguir esto [67]
            total = Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vianda_tamaño = models.ForeignKey(ViandaTamaño, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.vianda_tamaño.vianda.dia} - {self.vianda_tamaño.vianda.tipo} - {self.vianda_tamaño.tamaño.tamaño}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']