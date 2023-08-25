# Generated by Django 4.2.4 on 2023-08-23 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediacatalog',
            name='no_visualizaciones',
        ),
        migrations.RemoveField(
            model_name='mediacatalog',
            name='puntaje',
        ),
        migrations.CreateModel(
            name='MediaUsuariosCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_usuarios', models.IntegerField()),
                ('avg_score', models.FloatField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.mediacatalog')),
            ],
        ),
        migrations.CreateModel(
            name='MediaUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.FloatField(null=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.mediacatalog')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
