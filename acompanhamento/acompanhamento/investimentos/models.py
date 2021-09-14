from django.db import models

# Create your models here.

class Acao(models.Model):
    sigla = models.CharField(max_length=6)

