# Generated by Django 4.1.4 on 2023-02-02 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atracciones', '0002_atracciones_fotoatr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atracciones',
            old_name='codigoCiudadAtr',
            new_name='precioAtr',
        ),
    ]
