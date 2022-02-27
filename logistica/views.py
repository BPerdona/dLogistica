from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
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

    #Verificação de Termo
    if termo is None or not termo:
        return redirect('paciente')
    
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

    #Verificação de Termo
    if termo is None or not termo:
        return redirect('paciente')

    #Filtragem
    consultas = Consulta.objects.order_by('-id').filter(
        Q(paciente__nome_completo__icontains=termo) | Q(data_da_consulta__icontains=termo) | Q(hospital__icontains=termo),
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

def ver_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if not consulta.status_tupla:
        raise Http404
    return render(request, 'logistica/ver_consulta.html',{
        'consulta': consulta
    })