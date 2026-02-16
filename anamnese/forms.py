from django import forms
from .models import FichaAnamnese


class FichaAnamneseForm(forms.ModelForm):
    """Formulário completo para prontuário nutricional"""
    
    class Meta:
        model = FichaAnamnese
        exclude = ['data_criacao', 'arquivo_pdf', 'arquivo_docx', 'imc', 'relacao_cq']
        
        widgets = {
            # Identificação
            'data_consulta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profissão'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'motivo_consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Motivo da consulta'}),
            'observacoes_iniciais': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Observações iniciais'}),
            
            # Histórico Social
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'composicao_familiar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Mãe, pai, irmão'}),
            'quem_compra_alimentos': forms.TextInput(attrs={'class': 'form-control'}),
            'frequencia_compra': forms.Select(attrs={'class': 'form-control'}),
            'quem_prepara_refeicoes': forms.TextInput(attrs={'class': 'form-control'}),
            'com_quem_faz_refeicoes': forms.TextInput(attrs={'class': 'form-control'}),
            'bebidas_alcoolicas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Não / Sim, aos finais de semana'}),
            'fuma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Não / Sim, 10 cigarros/dia'}),
            
            # Objetivo
            'porque_procurou': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'meta_pessoal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Ganhar 10kg'}),
            
            # Sintomas - todos checkbox
            'vomito': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'vomito_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nausea': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nausea_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'mastigacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mastigacao_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'degluticao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'degluticao_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'digestao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'digestao_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'pirose': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pirose_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'refluxo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'refluxo_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'diarreia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'diarreia_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'obstipacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'obstipacao_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'insonia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'insonia_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'estresse': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'estresse_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'cansaco': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cansaco_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'ansiedade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ansiedade_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'depressao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'depressao_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'trabalho_estudo_afeta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trabalho_estudo_obs': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            
            # Outros dados clínicos
            'lesoes_pele': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'cirurgia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Não / Sim, apendicectomia em 2020'}),
            'habito_intestinal': forms.Select(attrs={'class': 'form-control'}),
            'consistencia_fezes': forms.Select(attrs={'class': 'form-control'}),
            'diurese': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'patologia': forms.TextInput(attrs={'class': 'form-control'}),
            'medicamento': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Antropometria
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'kg'}),
            'estatura': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'm'}),
            'circunferencia_braco_esq': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_braco_dir': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_peitoral': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_cintura': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_abdominal': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_quadril': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_coxa_dir': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_coxa_esq': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_panturrilha_esq': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_panturrilha_dir': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'circunferencia_pescoco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            
            # Dobras cutâneas
            'dc_triceps': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_biceps': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_escapula': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_suprailiaca': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_axilar_media': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_peitoral': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_abdominal': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_coxa_media': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'dc_panturrilha': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mm'}),
            'percentual_gordura': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': '%'}),
            
            # Estilo de Vida
            'nivel_atividade_fisica': forms.Select(attrs={'class': 'form-control'}),
            'qual_esporte': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Musculação, Corrida, Futebol'}),
            'frequencia_esporte': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3x por semana, Diariamente'}),
            
            # Diagnóstico
            'diagnostico_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico_etiologia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico_sinais': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            # Orientações
            'data_orientacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'orientacoes_texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'calculos_observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
