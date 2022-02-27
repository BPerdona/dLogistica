from urllib import request
from django.shortcuts import render
from logistica.models import Paciente, Consulta, Viagem, Motorista
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

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
    #Pegando o termo da URL de pesquisa
    termo = request.GET.get('termo')

    #Filtragem
    pacientes = Paciente.objects.order_by('-id').filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo) | Q(cpf__icontains = termo) | Q(cns__icontains = termo),
        status_tupla=True
    )

    #Paginação
    paginator = Paginator(pacientes, 10)
    page = request.GET.get('page')
    pacientes = paginator.get_page(page)

    #renderização da pagina
    return render(request, 'logistica/buscaPaciente.html', {
        'pacientes' : pacientes
    })

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

def buscaConsulta(request):
    #Pegando o termo da URL de pesquisa
    termo = request.GET.get('termo')

    #Falta realizar a consulta por nome

    #Filtragem
    consultas = Consulta.objects.order_by('-id').filter(
        Q(data_da_consulta__icontains=termo) | Q(hospital__icontains=termo),
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