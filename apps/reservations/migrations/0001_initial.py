# Generated by Django 5.2.4 on 2025-07-04 18:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('number', models.IntegerField(unique=True, verbose_name='Numero de mesa')),
                ('state', models.CharField(choices=[('D', 'Disponible'), ('O', 'Ocupada'), ('R', 'En Reserva')], default='D', max_length=3, verbose_name='Estado')),
                ('capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'Mesas',
                'ordering': ['capacity'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('reserved_at', models.DateTimeField(verbose_name='Hora de reserva')),
                ('duration_hours', models.IntegerField(verbose_name='Duracion de Reserva')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.table')),
            ],
            options={
                'db_table': 'Reservas',
            },
        ),
    ]
