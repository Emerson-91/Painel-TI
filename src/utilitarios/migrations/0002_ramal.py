# Generated by Django 5.1 on 2024-09-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilitarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ramal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_ramal', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('patrimonio', models.CharField(max_length=50)),
                ('ramal', models.CharField(max_length=20)),
                ('obs', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
