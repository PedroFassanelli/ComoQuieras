# Generated by Django 4.1.3 on 2022-11-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cometela', '0003_vianda_estado_vianda_fecha_alter_vianda_tamaño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vianda',
            name='dia',
            field=models.CharField(choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miercoles'), ('JUEVES', 'Jueves')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Dia',
        ),
    ]
