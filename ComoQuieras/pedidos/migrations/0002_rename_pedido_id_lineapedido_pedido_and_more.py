# Generated by Django 4.1.3 on 2022-11-18 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='vianda_tamaño_id',
            new_name='vianda_tamaño',
        ),
    ]