# Generated by Django 5.0.3 on 2024-04-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_documentos_autor'),
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='autor',
            field=models.ManyToManyField(related_name='%(class)s_requests_created', to='equipe.pesquisador'),
        ),
    ]
