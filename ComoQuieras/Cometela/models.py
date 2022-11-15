from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vianda(models.Model):
    DIAS = (
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miercoles'),
        ('JUEVES', 'Jueves')
    )
    dia = models.CharField(choices= DIAS, null=False, max_length=20)
    fecha = models.DateField(null=True)
    descripcion = models.CharField(max_length=250)
    Estados = (
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva')
    )
    estado = models.CharField(choices= Estados, max_length=20, null = True)

    Tipos = (
        ('TRADICIONAL', 'Tradicional'),
        ('VEGANA', 'Vegana'),
        ('LIGHT', 'Light')
    )
    tipo = models.CharField(choices= Tipos, max_length=20)
    
    Tamaños = (
        ('MEDIA', 'Media'),
        ('ENTERA', 'Entera')
    )
    tamaño = models.CharField(choices= Tamaños, max_length=20, null=True)

    precio = models.IntegerField()
    #precio_media = models.IntegerField()
    #precio_entera = models.IntegerField()

    def __str__(self):
        return f'{self.descripcion} {self.precio}'

#Vianda y Pedido deberia estar unificado?
class Pedido(models.Model):
    vianda = models.ForeignKey(Vianda, on_delete=models.DO_NOTHING)
    media = models.IntegerField(default=0)
    entera = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

