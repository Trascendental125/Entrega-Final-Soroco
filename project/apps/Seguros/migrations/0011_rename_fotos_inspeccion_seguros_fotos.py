# Generated by Django 4.2.2 on 2023-08-06 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seguros', '0010_rename_foto_inspeccion_seguros_fotos_inspeccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seguros',
            old_name='fotos_inspeccion',
            new_name='fotos',
        ),
    ]
