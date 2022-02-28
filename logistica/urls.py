from unicodedata import name
from django.urls import path
from . import views

#Url index
urlpatterns = [
    path('', views.index, name='index'),
]

#Urls de paciente
urlpatterns += [
    path('paciente/', views.listPaciente, name='paciente'),
    path('paciente/<int:paciente_id>', views.ver_paciente, name='ver_paciente'),
    path('paciente/busca/', views.buscaPaciente, name='busca_paciente'),
    path('paciente/cadastro/', views.cadastroPaciente, name='cadastro_paciente'),
]

#Urls de consulta
urlpatterns += [
    path('consulta/', views.listConsulta, name='consulta'),
    path('consulta/<int:consulta_id>', views.ver_consulta, name='ver_consulta'),
    path('consulta/busca', views.buscaConsulta, name='busca_consulta'),
    path('consulta/cadastro', views.cadastroConsulta, name='cadastro_consulta'),
]