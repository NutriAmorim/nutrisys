# Guia de Instalação - Sistema NutriSys

## 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

## 🚀 Instalação Passo a Passo

### 1. Baixar o Projeto

**Opção A - Com Git:**
```bash
git clone <seu-repositorio>
cd nutri_app
```

**Opção B - Download Manual:**
- Baixe e extraia o arquivo ZIP do projeto
- Abra o terminal na pasta extraída

### 2. Criar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Você verá `(venv)` no início da linha do terminal, indicando que o ambiente virtual está ativo.

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

Aguarde a instalação de todos os pacotes necessários.

### 4. Configurar o Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

Isso criará o banco de dados SQLite com todas as tabelas necessárias.

### 5. Criar Usuário Administrador

```bash
python manage.py createsuperuser
```

Preencha as informações solicitadas:
- Nome de usuário
- E-mail (pode deixar em branco)
- Senha (digite duas vezes)

### 6. Criar Diretórios de Media (opcional)

```bash
mkdir -p media/templates media/pdfs media/docs
```

### 7. Iniciar o Servidor

```bash
python manage.py runserver
```

O servidor iniciará em: http://127.0.0.1:8000

## 🎯 Acessando o Sistema

### Interface Principal
Abra seu navegador e acesse:
- **Página Inicial:** http://127.0.0.1:8000
- **Painel Admin:** http://127.0.0.1:8000/admin

### Usando o Sistema

1. **Criar Nova Ficha:**
   - Clique em "Nova Ficha"
   - Preencha todos os campos
   - Clique em "Gerar Ficha e PDF"

2. **Visualizar Fichas:**
   - Clique em "Minhas Fichas"
   - Veja todas as fichas criadas
   - Baixe o PDF de qualquer ficha

3. **Administração:**
   - Acesse /admin
   - Use o usuário criado no passo 5
   - Gerencie fichas pelo painel admin

## 📝 Template Word (Opcional)

Para usar templates Word personalizados:

1. Crie um arquivo Word (.docx) com sua ficha de anamnese
2. Use marcadores como:
   - `{{nome}}`
   - `{{idade}}`
   - `{{peso_atual}}`
   - `{{altura}}`
   - etc.
3. Salve em: `media/templates/ficha_anamnese_template.docx`

## ⚠️ Solução de Problemas

### Erro: "python não é reconhecido"
- Certifique-se de que Python está instalado
- Adicione Python ao PATH do sistema

### Erro: "No module named django"
- Ative o ambiente virtual
- Reinstale as dependências: `pip install -r requirements.txt`

### Erro ao gerar PDF
- Verifique se os diretórios media existem
- Verifique permissões de escrita

### Porta 8000 em uso
```bash
python manage.py runserver 8080
```

## 🔒 Segurança

**IMPORTANTE - Antes de colocar em produção:**

1. Mude a SECRET_KEY em `settings.py`
2. Configure `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use banco de dados PostgreSQL ou MySQL
5. Configure HTTPS

## 📦 Próximos Passos

Depois de instalar, você pode:
- [ ] Personalizar o template Word
- [ ] Adicionar sua planilha Excel com dados TACO
- [ ] Implementar cálculos de TMB/GET
- [ ] Adicionar sistema de plano alimentar

## 💡 Dicas

- Sempre ative o ambiente virtual antes de trabalhar no projeto
- Mantenha backups do banco de dados (db.sqlite3)
- Os PDFs ficam salvos em `media/pdfs/`

## 🆘 Precisa de Ajuda?

- Verifique o README.md
- Consulte a documentação do Django: https://docs.djangoproject.com
- Abra uma issue no GitHub
