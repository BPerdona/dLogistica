from re import search
from django.contrib import admin
from .models import Consulta, Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'rg', 'cpf', 'cns', 'status_tupla')
    list_display_links = ('id', 'nome_completo', 'rg', 'cns', 'cpf')
    search_fields = ('id', 'nome_completo', 'rg', 'cpf', 'cns')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_da_consulta', 'paciente', 'hospital', 'horario_da_consulta', 'status_tupla')
    list_display_links = ('id', 'data_da_consulta', 'paciente', 'hospital', 'horario_da_consulta')
    search_fields = ('id', 'data_da_consulta', 'hospital')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Consulta, ConsultaAdmin)
