# Como Criar o Template Word

## Instruções para criar sua ficha de anamnese personalizada

### 1. Abra o Microsoft Word

Crie um novo documento em branco.

### 2. Design da Ficha

Crie o layout da sua ficha como preferir. Exemplo:

```
═══════════════════════════════════════════════════════
              FICHA DE ANAMNESE NUTRICIONAL
═══════════════════════════════════════════════════════

DADOS PESSOAIS
Nome: {{nome}}
Data de Nascimento: {{data_nascimento}}
Idade: {{idade}} anos
Sexo: {{sexo}}
Telefone: {{telefone}}
E-mail: {{email}}
Profissão: {{profissao}}

DADOS ANTROPOMÉTRICOS
Peso Atual: {{peso_atual}}
Altura: {{altura}}
Peso Desejado: {{peso_desejado}}
IMC: {{imc}} - {{classificacao_imc}}

OBJETIVO
{{objetivo}}

HISTÓRIA CLÍNICA
Patologias/Doenças: {{patologias}}
Medicamentos em Uso: {{medicamentos}}
Alergias/Intolerâncias: {{alergias}}

ESTILO DE VIDA
Nível de Atividade Física: {{nivel_atividade}}
Refeições por Dia: {{refeicoes_dia}}
Consumo de Água: {{consumo_agua}}
Restrições Alimentares: {{restricoes}}

OBSERVAÇÕES
{{observacoes}}

═══════════════════════════════════════════════════════
Data de Criação: {{data_criacao}}
```

### 3. Marcadores Disponíveis

Use estes marcadores (exatamente como estão, com as chaves duplas):

**Dados Pessoais:**
- `{{nome}}` - Nome completo
- `{{data_nascimento}}` - Data de nascimento formatada
- `{{idade}}` - Idade em anos
- `{{sexo}}` - Masculino ou Feminino
- `{{telefone}}` - Número de telefone
- `{{email}}` - Endereço de e-mail
- `{{profissao}}` - Profissão

**Dados Antropométricos:**
- `{{peso_atual}}` - Peso em kg
- `{{altura}}` - Altura em metros
- `{{peso_desejado}}` - Peso desejado em kg
- `{{imc}}` - Valor do IMC calculado
- `{{classificacao_imc}}` - Classificação do IMC

**Objetivo:**
- `{{objetivo}}` - Objetivo nutricional

**História Clínica:**
- `{{patologias}}` - Patologias/doenças
- `{{medicamentos}}` - Medicamentos em uso
- `{{alergias}}` - Alergias/intolerâncias

**Estilo de Vida:**
- `{{nivel_atividade}}` - Nível de atividade física
- `{{refeicoes_dia}}` - Número de refeições por dia
- `{{consumo_agua}}` - Consumo de água em litros
- `{{restricoes}}` - Restrições alimentares

**Outros:**
- `{{observacoes}}` - Observações gerais
- `{{data_criacao}}` - Data de criação da ficha

### 4. Formatação

Você pode:
- Usar tabelas
- Adicionar logos e imagens (fixas)
- Formatar fontes, cores, tamanhos
- Adicionar cabeçalhos e rodapés
- Usar estilos do Word

### 5. Salvar o Template

1. Salve o documento como: `ficha_anamnese_template.docx`
2. Coloque na pasta: `media/templates/`
3. Caminho completo: `nutri_app/media/templates/ficha_anamnese_template.docx`

### 6. Testar

1. Crie uma nova ficha no sistema
2. O sistema preencherá automaticamente os marcadores
3. Gere o PDF para visualizar o resultado

## 💡 Dicas de Design

- Use cores profissionais (azul, verde, cinza)
- Adicione seu logo ou da clínica
- Separe seções com linhas ou cores
- Use negrito para destacar campos importantes
- Deixe espaço para assinaturas (físicas ou digitais)

## ⚠️ Importante

- Os marcadores devem estar exatamente como listados (com `{{` e `}}`)
- Não use espaços dentro dos marcadores
- Não mude o nome dos marcadores
- Teste sempre após criar/modificar o template

## 📄 Template Simples (Copie e Cole no Word)

Se preferir, copie este template básico:

═══════════════════════════════════════════════════════
FICHA DE ANAMNESE NUTRICIONAL
═══════════════════════════════════════════════════════

IDENTIFICAÇÃO
Nome: {{nome}}
DN: {{data_nascimento}} | Idade: {{idade}} anos | Sexo: {{sexo}}
Tel: {{telefone}} | E-mail: {{email}}
Profissão: {{profissao}}

AVALIAÇÃO ANTROPOMÉTRICA
Peso: {{peso_atual}} | Altura: {{altura}} | IMC: {{imc}} ({{classificacao_imc}})
Peso Desejado: {{peso_desejado}}
Objetivo: {{objetivo}}

ANAMNESE CLÍNICA
Patologias: {{patologias}}
Medicamentos: {{medicamentos}}
Alergias/Intolerâncias: {{alergias}}

HÁBITOS DE VIDA
Atividade Física: {{nivel_atividade}}
Refeições/dia: {{refeicoes_dia}} | Água: {{consumo_agua}}
Restrições: {{restricoes}}

OBSERVAÇÕES
{{observacoes}}

═══════════════════════════════════════════════════════
Documento gerado em: {{data_criacao}}
═══════════════════════════════════════════════════════
```
