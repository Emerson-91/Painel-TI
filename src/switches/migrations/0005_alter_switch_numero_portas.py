# Generated by Django 5.1 on 2024-12-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0004_switch_modelo_alter_switch_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='numero_portas',
            field=models.IntegerField(choices=[(24, '24 portas'), (48, '48 portas'), (52, '52 portas')]),
        ),
    ]
