from django.db import models
from equipe.models import Pesquisador

class Documentos(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Titulo da Monografia')
    autor = models.ManyToManyField(Pesquisador, related_name='autor_requests_created')
    orientador= models.ManyToManyField(Pesquisador, related_name='orientador_requests_created')
    coorientador = models.ManyToManyField(Pesquisador, related_name='coorientador_requests_created')
    resumo = models.TextField(verbose_name='Resumo')
    palavrasChaves = models.TextField(verbose_name='Palavras-chaves')
    dataEntrega = models.DateTimeField(verbose_name='Data de Entrega')
    arquivo = models.FileField(upload_to='pdfs/', blank=True, verbose_name='Documento em PDF')

    def __str__(self):
        autores = ', '.join([str(pesquisador) for pesquisador in self.autor.all()])
        return f"{self.titulo} ({self.palavrasChaves}) - Autores: {autores}"