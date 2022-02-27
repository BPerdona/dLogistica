from urllib import request
from django.shortcuts import render
from logistica.models import Paciente, Consulta, Viagem, Motorista
from django.core.paginator import Paginator

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
    #Filtragem
    pacientes = Paciente.objects.order_by('-id').filter(
        status_tupla=True
    )

    #Paginação
    paginator = Paginator(pacientes, 10)
    page = request.GET.get('page')
    pacientes = paginator.get_page(page)

    #renderização da pagina
    return render(request, 'logistica/paciente.html', {
        'pacientes' : pacientes
    })

def buscaPaciente(request):
    #renderização da pagina
    return render(request, 'logistica/buscaPaciente.html')

def listConsulta(request):
    #Filtragem
    consultas = Consulta.objects.order_by('-id').filter(
        status_tupla=True
    )

    #Paginação
    paginator = Paginator(consultas, 10)
    page = request.GET.get('page')
    consultas = paginator.get_page(page)

    #renderização da pagina
    return render(request, 'logistica/consulta.html', {
        'consultas' : consultas
    })