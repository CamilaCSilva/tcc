# Generated by Django 4.2.1 on 2023-05-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_remove_profissionaldesaude_senha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissionaldesaude',
            name='senha',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]