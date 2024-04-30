# Generated by Django 5.0.3 on 2024-04-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='areaConcentracao',
            field=models.CharField(blank=True, choices=[('Ciências Sociais e Humanas', 'Csh'), ('Ciências Exatas e Tecnológicas', 'Cet'), ('Ciências da Saúde', 'Cse'), ('Ciências Biológicas e Ambientais', 'Cba'), ('Artes e Comunicação', 'Aco'), ('Economia e Administração', 'Eao'), ('Educação', 'Edu'), ('Direito e Ciências Jurídicas', 'Dcj'), ('Tecnologia da Informação e Ciência da Computação', 'Tic')], max_length=50, null=True, verbose_name='Área de Concentração'),
        ),
    ]