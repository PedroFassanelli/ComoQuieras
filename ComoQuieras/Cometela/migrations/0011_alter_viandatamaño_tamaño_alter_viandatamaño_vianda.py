# Generated by Django 4.1.3 on 2022-11-29 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cometela', '0010_tamaño_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viandatamaño',
            name='tamaño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cometela.tamaño'),
        ),
        migrations.AlterField(
            model_name='viandatamaño',
            name='vianda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cometela.vianda'),
        ),
    ]
