# Generated by Django 4.1.3 on 2022-11-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cometela', '0005_viandatamaño_remove_vianda_precio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamaño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamaño', models.CharField(choices=[('MEDIA', 'Media'), ('ENTERA', 'Entera')], max_length=20, null=True)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='ViandaTamaño',
        ),
    ]
