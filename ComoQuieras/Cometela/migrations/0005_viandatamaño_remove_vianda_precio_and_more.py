# Generated by Django 4.1.3 on 2022-11-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cometela', '0004_alter_vianda_dia_delete_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViandaTamaño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamaño', models.CharField(choices=[('MEDIA', 'Media'), ('ENTERA', 'Entera')], max_length=20, null=True)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='vianda',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='vianda',
            name='tamaño',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.AddField(
            model_name='viandatamaño',
            name='vianda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Cometela.vianda'),
        ),
    ]
