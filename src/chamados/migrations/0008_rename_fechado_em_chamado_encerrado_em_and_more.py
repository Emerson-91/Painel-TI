# Generated by Django 5.1 on 2024-09-07 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0007_remove_chamado_encerrado_em_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chamado',
            old_name='fechado_em',
            new_name='encerrado_em',
        ),
        migrations.RenameField(
            model_name='chamado',
            old_name='usuario_fechamento',
            new_name='encerrado_por',
        ),
    ]
