from django.db import models

# Create your models here.

class Completed(models.Model):
    id = models.AutoField(primary_key=True)
    opcoes = models.CharField(max_length=20)

    def __str__(self):

        return self.opcoes

class Task(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    data = models.DateField()
    feita = models.ForeignKey(Completed, on_delete=models.PROTECT, default='2')

    def __str__(self):

        return self.titulo