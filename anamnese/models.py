from django.db import models
from django.utils import timezone


class FichaAnamnese(models.Model):
    """Modelo completo para prontuário nutricional"""
    
    # ========== IDENTIFICAÇÃO ==========
    data_consulta = models.DateField(default=timezone.now, verbose_name="Data da 1ª Consulta")
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    endereco = models.CharField(max_length=300, blank=True, verbose_name="Endereço")
    bairro = models.CharField(max_length=100, blank=True, verbose_name="Bairro")
    email = models.EmailField(verbose_name="E-mail")
    profissao = models.CharField(max_length=100, verbose_name="Profissão")
    celular = models.CharField(max_length=20, verbose_name="Celular")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    idade = models.IntegerField(verbose_name="Idade")
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name="Sexo")
    motivo_consulta = models.TextField(verbose_name="Motivo da Consulta")
    observacoes_iniciais = models.TextField(blank=True, verbose_name="Observações Iniciais")
    
    # ========== HISTÓRICO SOCIAL FAMILIAR ==========
    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
    ]
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado Civil")
    composicao_familiar = models.CharField(max_length=200, blank=True, verbose_name="Composição Familiar")
    quem_compra_alimentos = models.CharField(max_length=100, blank=True, verbose_name="Quem Compra os Alimentos")
    
    FREQUENCIA_COMPRA_CHOICES = [
        ('diariamente', 'Diariamente'),
        ('semanalmente', 'Semanalmente'),
        ('mensalmente', 'Mensalmente'),
    ]
    frequencia_compra = models.CharField(max_length=20, choices=FREQUENCIA_COMPRA_CHOICES, blank=True, verbose_name="Frequência da Compra")
    quem_prepara_refeicoes = models.CharField(max_length=100, blank=True, verbose_name="Quem Prepara as Refeições")
    com_quem_faz_refeicoes = models.CharField(max_length=100, blank=True, verbose_name="Com Quem Realiza as Refeições")
    bebidas_alcoolicas = models.CharField(max_length=200, blank=True, verbose_name="Uso de Bebidas Alcoólicas/Frequência")
    fuma = models.CharField(max_length=200, blank=True, verbose_name="Fuma ou Já Fumou / Quantidade")
    
    # ========== OBJETIVO PRINCIPAL ==========
    porque_procurou = models.TextField(verbose_name="Por que Procurou Atendimento")
    meta_pessoal = models.CharField(max_length=200, verbose_name="Meta Pessoal")
    
    # ========== DADOS CLÍNICOS - SINTOMAS ==========
    vomito = models.BooleanField(default=False, verbose_name="Vômito")
    vomito_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Vômito")
    nausea = models.BooleanField(default=False, verbose_name="Náusea")
    nausea_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Náusea")
    mastigacao = models.BooleanField(default=False, verbose_name="Dificuldade de Mastigação")
    mastigacao_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Mastigação")
    degluticao = models.BooleanField(default=False, verbose_name="Dificuldade de Deglutição")
    degluticao_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Deglutição")
    digestao = models.BooleanField(default=False, verbose_name="Problemas de Digestão")
    digestao_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Digestão")
    pirose = models.BooleanField(default=False, verbose_name="Pirose (Azia)")
    pirose_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Pirose")
    refluxo = models.BooleanField(default=False, verbose_name="Refluxo")
    refluxo_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Refluxo")
    diarreia = models.BooleanField(default=False, verbose_name="Diarreia")
    diarreia_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Diarreia")
    obstipacao = models.BooleanField(default=False, verbose_name="Obstipação (Prisão de Ventre)")
    obstipacao_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Obstipação")
    insonia = models.BooleanField(default=False, verbose_name="Insônia")
    insonia_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Insônia")
    estresse = models.BooleanField(default=False, verbose_name="Estresse")
    estresse_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Estresse")
    cansaco = models.BooleanField(default=False, verbose_name="Cansaço")
    cansaco_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Cansaço")
    ansiedade = models.BooleanField(default=False, verbose_name="Ansiedade")
    ansiedade_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Ansiedade")
    depressao = models.BooleanField(default=False, verbose_name="Depressão")
    depressao_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Depressão")
    trabalho_estudo_afeta = models.BooleanField(default=False, verbose_name="Trabalho/Estudo Afeta Bem-estar")
    trabalho_estudo_obs = models.CharField(max_length=200, blank=True, verbose_name="Obs. Trabalho/Estudo")
    
    # ========== DADOS CLÍNICOS - OUTROS ==========
    lesoes_pele = models.TextField(blank=True, verbose_name="Lesões/Problemas na Pele, Cabelo ou Unha")
    cirurgia = models.CharField(max_length=300, blank=True, verbose_name="Cirurgia (Sim/Não, Qual, Quando)")
    
    HABITO_INTESTINAL_CHOICES = [
        ('diario', 'Diário'),
        ('ate_3_dias', 'Até 3 dias'),
        ('mais_3_dias', 'Mais de 3 dias'),
        ('outros', 'Outros'),
    ]
    habito_intestinal = models.CharField(max_length=20, choices=HABITO_INTESTINAL_CHOICES, blank=True, verbose_name="Hábito Intestinal")
    
    CONSISTENCIA_FEZES_CHOICES = [
        ('normal', 'Normal'),
        ('amolecidas', 'Amolecidas'),
        ('duras', 'Duras'),
    ]
    consistencia_fezes = models.CharField(max_length=20, choices=CONSISTENCIA_FEZES_CHOICES, blank=True, verbose_name="Consistência das Fezes")
    diurese = models.TextField(blank=True, verbose_name="Diurese (Quantidade/Coloração)")
    patologia = models.CharField(max_length=300, blank=True, verbose_name="Patologia (Sim/Não, Qual, Desde Quando)")
    medicamento = models.CharField(max_length=300, blank=True, verbose_name="Medicamento (Sim/Não, Qual, Tempo)")
    
    # ========== FICHA ANTROPOMÉTRICA ==========
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    estatura = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Estatura (m)")
    imc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="IMC")
    circunferencia_braco_esq = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Braço Esquerdo (cm)")
    circunferencia_braco_dir = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Braço Direito (cm)")
    circunferencia_peitoral = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Peitoral (cm)")
    circunferencia_cintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Cintura (cm)")
    circunferencia_abdominal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Abdominal (cm)")
    circunferencia_quadril = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Quadril (cm)")
    circunferencia_coxa_dir = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Coxa Direita (cm)")
    circunferencia_coxa_esq = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Coxa Esquerda (cm)")
    circunferencia_panturrilha_esq = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Panturrilha Esq (cm)")
    circunferencia_panturrilha_dir = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Panturrilha Dir (cm)")
    circunferencia_pescoco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="C. Pescoço (cm)")
    relacao_cq = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, verbose_name="Relação C/Q")
    
    # Dobras cutâneas (podem ficar vazias)
    dc_triceps = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Tríceps (mm)")
    dc_biceps = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Bíceps (mm)")
    dc_escapula = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Escápula (mm)")
    dc_suprailiaca = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Suprailíaca (mm)")
    dc_axilar_media = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Axilar Média (mm)")
    dc_peitoral = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Peitoral (mm)")
    dc_abdominal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Abdominal (mm)")
    dc_coxa_media = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Coxa Média (mm)")
    dc_panturrilha = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="DC Panturrilha (mm)")
    percentual_gordura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="% Gordura")
    
    # ========== ESTILO DE VIDA ==========
    NIVEL_ATIVIDADE_CHOICES = [
        ('sedentario', 'Sedentário'),
        ('leve', 'Leve'),
        ('moderado', 'Moderado'),
        ('intenso', 'Intenso'),
    ]
    nivel_atividade_fisica = models.CharField(max_length=20, choices=NIVEL_ATIVIDADE_CHOICES, blank=True, verbose_name="Nível de Atividade Física")
    qual_esporte = models.CharField(max_length=200, blank=True, verbose_name="Qual Esporte Pratica")
    frequencia_esporte = models.CharField(max_length=100, blank=True, verbose_name="Quantas Vezes por Semana")
    
    # ========== DIAGNÓSTICO NUTRICIONAL ==========
    diagnostico_problema = models.TextField(blank=True, verbose_name="Problema")
    diagnostico_etiologia = models.TextField(blank=True, verbose_name="Etiologia")
    diagnostico_sinais = models.TextField(blank=True, verbose_name="Sinais/Sintomas")
    
    # ========== ORIENTAÇÕES ==========
    data_orientacao = models.DateField(blank=True, null=True, verbose_name="Data da Orientação")
    orientacoes_texto = models.TextField(blank=True, verbose_name="Orientações e Devolutivas")
    calculos_observacoes = models.TextField(blank=True, verbose_name="Cálculos e Observações")
    
    # ========== METADADOS ==========
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    arquivo_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True, verbose_name="PDF Gerado")
    arquivo_docx = models.FileField(upload_to='docs/', null=True, blank=True, verbose_name="Word Gerado")
    
    class Meta:
        verbose_name = "Prontuário Nutricional"
        verbose_name_plural = "Prontuários Nutricionais"
        ordering = ['-data_criacao']
    
    def __str__(self):
        return f"{self.nome} - {self.data_consulta.strftime('%d/%m/%Y')}"
    
    def calcular_imc(self):
        """Calcula o IMC automaticamente"""
        if self.peso and self.estatura:
            imc_calc = float(self.peso) / (float(self.estatura) ** 2)
            return round(imc_calc, 2)
        return None
    
    def calcular_relacao_cq(self):
        """Calcula relação cintura/quadril"""
        if self.circunferencia_cintura and self.circunferencia_quadril:
            return round(float(self.circunferencia_cintura) / float(self.circunferencia_quadril), 2)
        return None
    
    def classificacao_imc(self):
        """Classificação do IMC"""
        imc = self.calcular_imc()
        if not imc:
            return "N/A"
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Eutrófico"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        elif 30 <= imc < 35:
            return "Obesidade Grau I"
        elif 35 <= imc < 40:
            return "Obesidade Grau II"
        else:
            return "Obesidade Grau III"
    
    def save(self, *args, **kwargs):
        """Calcula IMC e relação C/Q automaticamente ao salvar"""
        if not self.imc:
            self.imc = self.calcular_imc()
        if not self.relacao_cq:
            self.relacao_cq = self.calcular_relacao_cq()
        super().save(*args, **kwargs)
