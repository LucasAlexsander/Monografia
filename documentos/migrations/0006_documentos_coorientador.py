# Generated by Django 5.0.3 on 2024-04-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_documentos_orientador'),
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='coorientador',
            field=models.ManyToManyField(related_name='coorientador_requests_created', to='equipe.pesquisador'),
        ),
    ]
