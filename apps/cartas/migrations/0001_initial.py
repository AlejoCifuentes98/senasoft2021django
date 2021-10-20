# Generated by Django 3.2.8 on 2021-10-20 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas_Ocultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carta_des', models.PositiveSmallIntegerField()),
                ('carta_mod', models.PositiveSmallIntegerField()),
                ('carta_err', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cartas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartas.tipo')),
            ],
        ),
    ]
