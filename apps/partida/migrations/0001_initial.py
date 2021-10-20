# Generated by Django 3.2.8 on 2021-10-20 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ingreso', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Anotacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partida.jugadores')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partida.partida')),
            ],
        ),
    ]
