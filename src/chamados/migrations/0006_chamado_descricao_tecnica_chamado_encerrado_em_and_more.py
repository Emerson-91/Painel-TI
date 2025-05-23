# Generated by Django 5.1 on 2024-09-07 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0005_departamento_ativo_local_ativo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='descricao_tecnica',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chamado',
            name='encerrado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chamado',
            name='encerrado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chamado',
            name='nr_patrimonio',
            field=models.CharField(default='padrao', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamado',
            name='solucao_tecnica',
            field=models.TextField(blank=True, null=True),
        ),
    ]
