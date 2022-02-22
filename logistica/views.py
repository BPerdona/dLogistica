from urllib import request
from django.shortcuts import render

def index(request):
    return render(request, 'logistica/index.html')