# Generated by Django 4.2.4 on 2023-08-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_remove_mediacatalog_no_visualizaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacatalog',
            name='genero',
            field=models.CharField(choices=[('fantasia', 'Fantasia'), ('accion', 'Accion'), ('comedia', 'Comedia'), ('terror', 'Terror'), ('drama', 'Drama'), ('infantil', 'Infantil')], max_length=255),
        ),
    ]