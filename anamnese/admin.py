from django.contrib import admin
from .models import FichaAnamnese


@admin.register(FichaAnamnese)
class FichaAnamneseAdmin(admin.ModelAdmin):

    list_display = [
        'nome',
        'idade',
        'sexo',
        'meta_pessoal',
        'calcular_imc',
        'data_criacao'
    ]

    list_filter = [
        'sexo',
        'estado_civil',
        'data_consulta',
        'data_criacao'
    ]

    search_fields = [
        'nome',
        'email',
        'celular'
    ]

    date_hierarchy = 'data_criacao'

    readonly_fields = ['data_criacao', 'imc', 'relacao_cq']
