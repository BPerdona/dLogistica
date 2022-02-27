from audioop import maxpp
from pyexpat import model
from django.db import models
from django.urls import reverse

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=150)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=12)
    cns = models.CharField(max_length=20)
    data_de_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15)
    status_tupla = models.BooleanField(default=True)

    def __str__(self) :
        return self.nome_completo

class Consulta(models.Model):
    data_da_consulta = models.DateField()
    hospital = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    horario_da_consulta = models.CharField(max_length=20)
    acompanhante = models.CharField(max_length=200)
    local_de_espera = models.TextField(max_length=5000)
    status_tupla = models.BooleanField(default=True)

    def __str__(self):
        return f'Hospital: {self.hospital} Data: {self.data_da_consulta} Paciente: {self.paciente.nome}'

class Motorista(models.Model):
    nome = models.CharField(max_length=150)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=12)
    data_de_nascimento = models.DateField()
    status_tupla = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Viagem(models.Model):
    data_da_viagem = models.DateField()
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)
    consultas = models.ManyToManyField(Consulta, help_text="Selecione as consultas que iram nessa viagem.")
    horario_de_saida = models.CharField(max_length=20)
    destino: models.CharField(max_length=30)
    status_tupla = models.BooleanField(default=True)

    def __str__(self):
        return f'Data: {self.data_da_viagem} Motorista: {self.motorista.nome}'