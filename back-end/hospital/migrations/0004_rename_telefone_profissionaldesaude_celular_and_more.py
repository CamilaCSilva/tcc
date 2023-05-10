# Generated by Django 4.2 on 2023-05-06 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_fichapaciente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profissionaldesaude',
            old_name='telefone',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='profissionaldesaude',
            old_name='documentoTrabalho',
            new_name='documento_trabalho',
        ),
        migrations.RenameField(
            model_name='profissionaldesaude',
            old_name='nomeCompleto',
            new_name='nome_completo',
        ),
        migrations.RenameField(
            model_name='profissionaldesaude',
            old_name='unidadeDeAtendimento',
            new_name='unidade_de_atendimento',
        ),
    ]