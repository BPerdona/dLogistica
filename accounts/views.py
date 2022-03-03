from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('login')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('login')