# Generated by Django 5.1 on 2024-10-26 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('numero_portas', models.IntegerField(choices=[(24, '24 portas'), (48, '48 portas')])),
                ('poe', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PortaSwitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_porta', models.PositiveIntegerField()),
                ('vlan', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=100)),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portas', to='switches.switch')),
            ],
        ),
    ]
