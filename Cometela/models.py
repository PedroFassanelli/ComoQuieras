from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Vianda(models.Model):
    DIAS = (
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miercoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes')
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
        ('VEGGIE', 'Veggie'),
        ('LIGHT', 'Light')
    )
    tipo = models.CharField(choices= Tipos, max_length=20)

    def __str__(self):
        return f'{self.dia} - {self.fecha} - {self.tipo}'

class Tamaño(models.Model):
    Tamaños = (
        ('MEDIA', 'Media'),
        ('ENTERA', 'Entera')
    )
    tamaño = models.CharField(choices= Tamaños, max_length=20, null=True)
    precio = models.IntegerField(default=0)
    Estados = (
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva')
    )
    estado = models.CharField(choices= Estados, max_length=20, null = True)

    def __str__(self):
        return f'{self.tamaño} - {self.precio}'

class ViandaTamaño(models.Model):
    vianda = models.ForeignKey(Vianda, on_delete=models.CASCADE)
    tamaño = models.ForeignKey(Tamaño, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vianda} - {self.tamaño}'
        
#Creamos las ViandaTamaño automaticamente cuando se crea una vianda
def create_vianda_tamaño(sender, instance, created, **kwargs):
    if created:
        ViandaTamaño.objects.create(vianda=instance, tamaño=Tamaño.objects.filter(estado='ACTIVA').filter(tamaño='MEDIA')[0])
        ViandaTamaño.objects.create(vianda=instance, tamaño=Tamaño.objects.filter(estado='ACTIVA').filter(tamaño='ENTERA')[0])

post_save.connect(create_vianda_tamaño, sender=Vianda)
                
