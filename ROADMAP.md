# ROADMAP - Sistema NutriSys

## ✅ Fase 1 - CONCLUÍDA
**Ficha de Anamnese Digital**

- [x] Formulário web completo
- [x] Validação de dados
- [x] Geração automática de PDF
- [x] Preenchimento de template Word
- [x] Sistema CRUD (criar, ler, atualizar, deletar)
- [x] Cálculo de IMC
- [x] Interface responsiva e moderna
- [x] Painel administrativo

## 🔄 Fase 2 - EM PLANEJAMENTO
**Importação de Dados e Tabelas Nutricionais**

### 2.1 Tabela TACO
- [ ] Importar dados da tabela TACO (composição de alimentos)
- [ ] Criar modelo de banco de dados para alimentos
- [ ] Interface para buscar alimentos
- [ ] Filtros por categoria, nutriente, nome

### 2.2 Cadastro de Alimentos Consumidos
- [ ] Sistema para registrar alimentos consumidos
- [ ] Tabela de proporções alimentares
- [ ] Conversão de medidas caseiras para gramas
- [ ] Histórico de consumo

### 2.3 Recordatório Alimentar
- [ ] Formulário de recordatório 24h
- [ ] Registro por refeição (café, almoço, jantar, lanches)
- [ ] Cálculo automático de calorias e macros
- [ ] Relatórios de consumo

**Estrutura de Banco de Dados:**
```python
class Alimento(models.Model):
    codigo_taco = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    energia_kcal = models.DecimalField(max_digits=8, decimal_places=2)
    proteinas_g = models.DecimalField(max_digits=8, decimal_places=2)
    lipidios_g = models.DecimalField(max_digits=8, decimal_places=2)
    carboidratos_g = models.DecimalField(max_digits=8, decimal_places=2)
    fibras_g = models.DecimalField(max_digits=8, decimal_places=2)
    # ... outros nutrientes

class Recordatorio(models.Model):
    ficha = models.ForeignKey(FichaAnamnese, on_delete=models.CASCADE)
    data = models.DateField()
    refeicao = models.CharField(max_length=50)  # café, almoço, etc
    
class ItemRecordatorio(models.Model):
    recordatorio = models.ForeignKey(Recordatorio, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    quantidade_g = models.DecimalField(max_digits=8, decimal_places=2)
    # campos calculados automaticamente
    energia_total = models.DecimalField(max_digits=8, decimal_places=2)
    proteinas_total = models.DecimalField(max_digits=8, decimal_places=2)
    # etc
```

## 🎯 Fase 3 - FUTURO
**Cálculos Nutricionais Avançados**

### 3.1 TMB e GET
- [ ] Cálculo de Taxa Metabólica Basal (TMB)
  - Fórmula Harris-Benedict
  - Fórmula Mifflin-St Jeor
  - Comparação entre fórmulas
- [ ] Cálculo de Gasto Energético Total (GET)
  - TMB × Fator de Atividade
  - Ajuste por objetivo (perda/ganho/manutenção)

### 3.2 Análise de Déficit/Superávit
- [ ] Comparar consumo vs necessidade
- [ ] Indicador visual de déficit/superávit
- [ ] Alertas e recomendações
- [ ] Gráficos de progresso

### 3.3 Distribuição de Macronutrientes
- [ ] Cálculo de macros por objetivo
- [ ] Percentuais recomendados
- [ ] Ajustes personalizados
- [ ] Visualização em gráficos

**Exemplo de Cálculo TMB:**
```python
def calcular_tmb(ficha):
    """
    Harris-Benedict:
    Homens: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × idade)
    Mulheres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × idade)
    """
    peso = float(ficha.peso_atual)
    altura_cm = float(ficha.altura) * 100
    idade = ficha.idade
    
    if ficha.sexo == 'M':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura_cm) - (5.677 * idade)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura_cm) - (4.330 * idade)
    
    return round(tmb, 2)

def calcular_get(ficha):
    """GET = TMB × Fator de Atividade"""
    tmb = calcular_tmb(ficha)
    
    fatores = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'intenso': 1.725,
    }
    
    fator = fatores[ficha.nivel_atividade]
    get = tmb * fator
    
    # Ajustar por objetivo
    if ficha.objetivo == 'perda':
        get *= 0.8  # déficit de 20%
    elif ficha.objetivo == 'ganho':
        get *= 1.15  # superávit de 15%
    
    return round(get, 2)
```

## 🍽️ Fase 4 - FUTURO
**Plano Alimentar Personalizado**

### 4.1 Gerador de Plano
- [ ] Criar plano baseado em objetivo
- [ ] Distribuir calorias por refeição
- [ ] Sugerir alimentos da tabela TACO
- [ ] Respeitar restrições e preferências

### 4.2 Templates de Planos
- [ ] Planos pré-definidos
- [ ] Planos vegetarianos/veganos
- [ ] Planos para diabéticos
- [ ] Planos para hipertensão

### 4.3 Lista de Compras
- [ ] Gerar lista automática
- [ ] Organizar por categoria
- [ ] Calcular quantidades
- [ ] Exportar para PDF

## 📊 Fase 5 - FUTURO
**Relatórios e Acompanhamento**

### 5.1 Dashboard
- [ ] Resumo do paciente
- [ ] Gráficos de evolução
- [ ] Alertas nutricionais
- [ ] Metas e progresso

### 5.2 Comparativos
- [ ] Comparar períodos
- [ ] Análise de tendências
- [ ] Relatórios personalizados
- [ ] Exportação de dados

### 5.3 Evolução do Paciente
- [ ] Histórico de peso
- [ ] Histórico de medidas
- [ ] Fotos de progresso
- [ ] Anotações do nutricionista

## 🔧 Melhorias Técnicas Futuras

### Backend
- [ ] API REST com Django REST Framework
- [ ] Autenticação JWT
- [ ] Sistema de permissões
- [ ] Backup automático

### Frontend
- [ ] App mobile (React Native)
- [ ] PWA (Progressive Web App)
- [ ] Modo offline
- [ ] Notificações push

### Integrações
- [ ] Integração com balanças inteligentes
- [ ] Integração com apps de exercício
- [ ] Export para Excel avançado
- [ ] Sincronização na nuvem

## 📅 Cronograma Estimado

- **Fase 1:** ✅ CONCLUÍDA
- **Fase 2:** 2-3 meses
- **Fase 3:** 1-2 meses
- **Fase 4:** 2-3 meses
- **Fase 5:** 1-2 meses

## 🎯 Objetivos de Cada Fase

### Fase 2
Permitir que você importe seus dados do Excel e comece a trabalhar com a tabela TACO dentro do sistema.

### Fase 3
Automatizar todos os cálculos nutricionais que você faz hoje na planilha.

### Fase 4
Gerar planos alimentares personalizados automaticamente.

### Fase 5
Acompanhar a evolução dos pacientes ao longo do tempo.

## 💡 Como Contribuir

Se você quiser começar a desenvolver alguma funcionalidade:

1. Escolha uma tarefa da fase atual
2. Crie uma branch: `git checkout -b feature/nome-da-funcionalidade`
3. Desenvolva e teste
4. Faça commit: `git commit -m "Adiciona funcionalidade X"`
5. Push: `git push origin feature/nome-da-funcionalidade`
6. Abra um Pull Request

## 📞 Próximos Passos Imediatos

Para começar a Fase 2, você precisará:

1. **Arquivo da Tabela TACO:**
   - Formato: CSV ou Excel
   - Colunas: código, nome, categoria, nutrientes
   
2. **Sua Planilha Excel Atual:**
   - Para entender a estrutura
   - Para migrar dados existentes

3. **Definir Prioridades:**
   - Qual funcionalidade é mais importante?
   - Recordatório ou TMB/GET primeiro?

**Quando estiver pronto para a Fase 2, me envie sua planilha e podemos começar!**
