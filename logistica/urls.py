from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paciente/', views.listPaciente, name='paciente'),
    path('paciente/busca/', views.buscaPaciente, name='busca_paciente'),
    path('consulta/', views.listConsulta, name='consulta'),
    path('consulta/busca', views.buscaConsulta, name='busca_consulta')
]