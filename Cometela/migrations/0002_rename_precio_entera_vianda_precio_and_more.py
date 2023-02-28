# Generated by Django 4.1.3 on 2022-11-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cometela', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vianda',
            old_name='precio_entera',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='vianda',
            name='precio_media',
        ),
        migrations.AddField(
            model_name='vianda',
            name='tamaño',
            field=models.CharField(choices=[('MEDIA', 'Media'), ('ENTERA', 'Media')], max_length=20, null=True),
        ),
    ]
