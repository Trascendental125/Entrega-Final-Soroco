# Generated by Django 4.2.2 on 2023-07-23 23:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Seguros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seguro',
            old_name='categoria',
            new_name='seccion',
        ),
        migrations.RenameField(
            model_name='seguro',
            old_name='cantidad',
            new_name='suma',
        ),
        migrations.RenameField(
            model_name='segurocategoria',
            old_name='nombre',
            new_name='seccion',
        ),
        migrations.RemoveField(
            model_name='seguro',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='seguro',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='seguro',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='seguro',
            name='unidad_de_medida',
        ),
        migrations.AddField(
            model_name='seguro',
            name='fecha_suscripcion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='fecha de suscripcion'),
        ),
    ]
