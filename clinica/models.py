from django.db import models
from django.utils import timezone
from django.urls import reverse

class Setor(models.Model):
    setor = models.CharField(max_length=100)

    def __str__(self):
        return self.setor

class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    data_nasc = models.DateTimeField(blank=True, null=True)
    rg = models.CharField(max_length=10, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=10)
    celular = models.CharField(max_length=11)
    cep = models.CharField(max_length=20)
    linha1 = models.CharField(max_length=150, verbose_name='Endereço', blank=True, null=True)
    linha2 = models.CharField(max_length=150, verbose_name='Complemento', blank=True, null=True)
    setor = models.ForeignKey(Setor, models.SET_NULL, blank=True, null=True)
    descricao = models.TextField(max_length=255)
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)
    create_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return "/clinica/%i/" % self.id



class Paciente(models.Model):
    paciente = models.ForeignKey(Pessoa, models.SET_NULL, blank=True, null=True)
    descricao = models.TextField(max_length=255)
    Create_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.paciente

    def get_absolute_url(self):
        return "/%i/" % self.id
