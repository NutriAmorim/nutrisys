# 🚀 INÍCIO RÁPIDO - Sistema NutriSys

## O que foi criado?

✅ **Sistema Web Django completo** para gestão de fichas de anamnese nutricional
✅ **Formulário web** para coletar dados dos pacientes
✅ **Geração automática de PDF** profissional
✅ **Preenchimento de documentos Word** (template personalizável)
✅ **Interface moderna e responsiva** com Bootstrap
✅ **Sistema CRUD completo** (criar, visualizar, editar, deletar)
✅ **Cálculo automático de IMC** com classificação

## 📁 Estrutura do Projeto

```
nutri_app/
├── 📖 README.md              - Documentação completa
├── 📖 INSTALL.md             - Guia de instalação passo a passo
├── 📖 ROADMAP.md             - Próximas funcionalidades (Fase 2, 3, 4...)
├── 📖 GITHUB_GUIDE.md        - Como subir para GitHub
├── 📖 TEMPLATE_WORD_GUIDE.md - Como criar templates Word
│
├── 🔧 setup.bat              - Instalação automática (Windows)
├── 🔧 setup.sh               - Instalação automática (Linux/Mac)
├── 📦 requirements.txt       - Dependências Python
│
├── 🎯 manage.py              - Comando principal Django
├── ⚙️ nutri_system/          - Configurações do projeto
│   ├── settings.py          - Configurações gerais
│   ├── urls.py              - Rotas principais
│   └── wsgi.py              - Servidor WSGI
│
├── 💊 anamnese/              - App principal
│   ├── models.py            - Banco de dados (FichaAnamnese)
│   ├── views.py             - Lógica das páginas
│   ├── forms.py             - Formulários
│   ├── urls.py              - Rotas do app
│   ├── admin.py             - Painel administrativo
│   ├── utils.py             - Funções PDF e Word
│   └── templates/           - Páginas HTML
│       ├── base.html        - Template base
│       ├── home.html        - Formulário
│       ├── lista_fichas.html
│       ├── visualizar_ficha.html
│       ├── editar_ficha.html
│       └── deletar_ficha.html
│
└── 📁 media/                 - Arquivos gerados
    ├── pdfs/                - PDFs das fichas
    ├── docs/                - Documentos Word
    └── templates/           - Templates Word personalizados
```

## ⚡ Instalação Ultra-Rápida

### Windows
1. Abra o terminal na pasta `nutri_app`
2. Execute: `setup.bat`
3. Siga as instruções
4. Acesse: http://127.0.0.1:8000

### Linux/Mac
1. Abra o terminal na pasta `nutri_app`
2. Execute: `./setup.sh`
3. Siga as instruções
4. Acesse: http://127.0.0.1:8000

## 📖 Instalação Manual

Se preferir fazer passo a passo, veja o arquivo `INSTALL.md`

## 🎯 Como Usar

### 1️⃣ Criar Nova Ficha
- Acesse http://127.0.0.1:8000
- Clique em "Nova Ficha"
- Preencha todos os campos do formulário
- Clique em "Gerar Ficha e PDF"
- ✅ PDF será gerado automaticamente!

### 2️⃣ Visualizar Fichas
- Acesse http://127.0.0.1:8000/fichas
- Veja todas as fichas criadas
- Clique em qualquer ficha para ver detalhes
- Baixe o PDF a qualquer momento

### 3️⃣ Editar/Deletar
- Na lista de fichas, clique em "Editar" ou "Deletar"
- Faça as alterações necessárias
- O PDF será regenerado automaticamente

### 4️⃣ Painel Admin (Avançado)
- Acesse http://127.0.0.1:8000/admin
- Use o usuário criado no setup
- Gerencie fichas, visualize relatórios

## 🎨 Personalizar Template Word

1. Crie um documento Word (.docx)
2. Use marcadores como `{{nome}}`, `{{peso_atual}}`, etc.
3. Salve em `media/templates/ficha_anamnese_template.docx`
4. Veja `TEMPLATE_WORD_GUIDE.md` para lista completa

## 🌐 Subir para GitHub

1. Crie repositório no GitHub
2. Siga o guia em `GITHUB_GUIDE.md`
3. Execute os comandos git
4. Pronto! Seu código está no GitHub

## 📊 Funcionalidades Atuais (Fase 1)

✅ Dados Pessoais (nome, idade, contato, profissão)
✅ Dados Antropométricos (peso, altura, IMC)
✅ Objetivo (perda de peso, ganho de massa, etc)
✅ História Clínica (patologias, medicamentos, alergias)
✅ Estilo de Vida (atividade física, refeições, água)
✅ Observações gerais
✅ Geração de PDF profissional
✅ Preenchimento de Word (opcional)
✅ Interface moderna e responsiva
✅ Sistema completo de CRUD

## 🔮 Próximas Fases

### Fase 2 - Tabelas Nutricionais
- [ ] Importar tabela TACO
- [ ] Cadastro de alimentos consumidos
- [ ] Recordatório alimentar 24h
- [ ] Cálculo de calorias e macros

### Fase 3 - Cálculos Avançados
- [ ] TMB (Taxa Metabólica Basal)
- [ ] GET (Gasto Energético Total)
- [ ] Análise de déficit/superávit
- [ ] Distribuição de macronutrientes

### Fase 4 - Plano Alimentar
- [ ] Gerador de plano personalizado
- [ ] Sugestões de alimentos
- [ ] Lista de compras
- [ ] Templates de planos

Veja `ROADMAP.md` para detalhes completos!

## 🆘 Problemas Comuns

**"python não é reconhecido"**
→ Instale Python 3.10+ e adicione ao PATH

**"No module named django"**
→ Ative o ambiente virtual: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)

**Erro ao gerar PDF**
→ Verifique se a pasta `media/pdfs` existe

**Porta 8000 em uso**
→ Use outra porta: `python manage.py runserver 8080`

## 📞 Suporte

- 📖 Veja INSTALL.md para instalação detalhada
- 🗺️ Veja ROADMAP.md para próximas funcionalidades
- 🌐 Veja GITHUB_GUIDE.md para GitHub
- 📝 Veja TEMPLATE_WORD_GUIDE.md para templates

## 🎉 Pronto para Começar!

```bash
# 1. Entre na pasta
cd nutri_app

# 2. Execute o setup
setup.bat    # Windows
./setup.sh   # Linux/Mac

# 3. Acesse no navegador
# http://127.0.0.1:8000

# 4. Divirta-se! 🚀
```

## 📸 Demo

Quando estiver rodando, você verá:
- 🏠 Página inicial com formulário bonito
- 📋 Lista de fichas em cards
- 👁️ Visualização completa da ficha
- 📥 Download de PDF com um clique
- ✏️ Edição fácil
- 🗑️ Confirmação antes de deletar

## 🎯 Objetivo Final

Substituir completamente sua planilha Excel por um sistema web moderno, automático e profissional!

**Fase 1 (ATUAL):** ✅ Ficha de anamnese digital
**Próxima Fase:** 🔄 Cálculos nutricionais e tabela TACO

---

**Desenvolvido com ❤️ para nutricionistas**

🌟 Se gostou, dê uma estrela no GitHub!
🐛 Achou um bug? Abra uma issue!
💡 Tem uma ideia? Compartilhe!
