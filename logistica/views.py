from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from logistica.models import Paciente, Consulta, Viagem, Motorista
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

def index(request):
    messages.add_message(request, messages.ERROR, 'DEU RUIM PIA')

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
        return redirect('consulta')

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

def ver_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if not paciente.status_tupla:
        raise Http404
    consultas = Consulta.objects.filter(paciente_id=paciente)

    return render(request, 'logistica/ver_paciente.html',{
        'paciente': paciente,
        'consulta': consultas
    })

def cadastroPaciente(request):
    if request.method != 'POST':
        return render(request, 'logistica/cadastroPaciente.html')
    
    Cnome = request.POST.get('nome')
    Crg = request.POST.get('rg')
    Ccpf = request.POST.get('cpf')
    Cdata_nascimento = request.POST.get('data')
    Ccns = request.POST.get('cns')
    Ctelefone = request.POST.get('telefone')

    #Validando todos os campos
    if not Cnome or not Crg or not Ccpf or not Cdata_nascimento or not Ccns or not Ctelefone:
        messages.add_message(request, messages.ERROR, 'Todos os campos devem ser preenchidos')
        return render(request, 'logistica/cadastroPaciente.html')

    if not Crg.isnumeric() or not Ccpf.isnumeric() or not Ccns.isnumeric():
        messages.add_message(request, messages.ERROR, 'Digite apenas numeros nos campos: "RG" "CPF" "CNS".')
        return render(request, 'logistica/cadastroPaciente.html')

    if not Crg.isnumeric() or not Ccpf.isnumeric() or not Ccns.isnumeric():
        return render(request, 'logistica/cadastroPaciente.html')
        # adicionar mensagem de retorno fracasso

    #Validando para ver se o nome já existe
    if Paciente.objects.filter(nome_completo=Cnome, status_tupla=True).exists():
        messages.add_message(request, messages.ERROR, 'Esse nome de usuario já existe no sistema!')
        return render(request, 'logistica/cadastroPaciente.html')
        

    #Validando para ver se o CPF já existe
    if Paciente.objects.filter(cpf=Ccpf, status_tupla=True).exists():
        messages.add_message(request, messages.ERROR, 'Esse CPF já está cadastrado no sistema')
        return render(request, 'logistica/cadastroPaciente.html')


    #Validando para ver se o RG já existe
    if Paciente.objects.filter(rg=Crg, status_tupla=True).exists():
        messages.add_message(request, messages.ERROR, 'Esse RG já está cadastrado no sistema')
        return render(request, 'logistica/cadastroPaciente.html')

    #Salvando objeto
    obj = Paciente.objects.create(nome_completo=Cnome, rg=Crg, cpf=Ccpf, cns=Ccns, data_de_nascimento=Cdata_nascimento, telefone=Ctelefone)
    paciente = get_object_or_404(Paciente, nome_completo=Cnome)
    messages.add_message(request, messages.SUCCESS, 'Paciente cadastrado com sucesso!')
    return redirect('ver_paciente', paciente.pk)

def cadastroConsulta(request):
    pacientes = Paciente.objects.filter(
        status_tupla=True
    )

    if request.method != 'POST':
        return render(request, 'logistica/cadastroConsulta.html', {
            'pacientes' : pacientes
        })
    
    Cdata = request.POST.get('data')
    Chospital = request.POST.get('hospital')
    Cpaciente = request.POST.get('paciente')
    Chorario = request.POST.get('horario')
    Cacompanhante = request.POST.get('acompanhante')
    Clocal = request.POST.get('local')

    #Cast de string para Int
    if Cpaciente == "Escolha":
        return render(request, 'logistica/cadastroConsulta.html', {
            'pacientes': pacientes
        })
    Cpaciente = int(Cpaciente)

    pacienteSele = get_object_or_404(Paciente, id=Cpaciente)

    #Validando todos os campos
    if not Cdata or not Chospital or not Cpaciente or not Chorario or not Cacompanhante or not Clocal:
        messages.add_message(request, messages.ERROR, 'Todos os campos devem ser preenchidos.')
        return render(request, 'logistica/cadastroConsulta.html', {
            'pacientes': pacientes
        })

    obj = Consulta.objects.create(data_da_consulta=Cdata, hospital=Chospital, paciente=pacienteSele, horario_da_consulta=Chorario, acompanhante=Cacompanhante, local_de_espera=Clocal)
    messages.add_message(request, messages.SUCCESS, 'Consulta cadastrada com sucesso.')
    return redirect('ver_paciente', Cpaciente)