# Generated by Django 5.0.3 on 2024-04-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_alter_documentos_autor'),
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='orientador',
            field=models.ManyToManyField(related_name='orientador_requests_created', to='equipe.pesquisador'),
        ),
    ]