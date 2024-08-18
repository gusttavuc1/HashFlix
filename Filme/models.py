from django.db import models

# Create your models here.
#Criar um Filme
from django.db import models
from django.utils import timezone

#Criar a Tabela Filme


list_categories = (
    ('analises', 'Análises'),
    ('apresentacao', 'Apresentação'),
    ('programacao', 'Programação')
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=5000)
    categoria = models.CharField(max_length=30, choices=list_categories)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.titulo
    