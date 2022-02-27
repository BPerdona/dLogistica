from urllib import request
from django.shortcuts import render
from logistica.models import Paciente, Consulta, Viagem, Motorista

def index(request):
    qtd_pacientes = Paciente.objects.count()
    qtd_consultas = Consulta.objects.count()
    qtd_viagens = Viagem.objects.count()
    qtd_motoristas = Motorista.objects.count()

    context = {
        'qtd_pacientes': qtd_pacientes,
        'qtd_consultas': qtd_consultas,
        'qtd_viagens': qtd_viagens,
        'qtd_motoristas': qtd_motoristas
    }

    return render(request, 'logistica/index.html', context)

def listPaciente(request):
    pacientes = Paciente.objects.order_by('-id').filter(
        status_tupla=True
    )
    return render(request, 'logistica/paciente.html', {
        'pacientes' : pacientes
    })