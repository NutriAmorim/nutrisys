# Guia de Deploy no GitHub

## 📦 Subir o Projeto para o GitHub

### 1. Criar Repositório no GitHub

1. Acesse https://github.com
2. Clique em "New repository"
3. Nome: `nutrisys` (ou outro de sua preferência)
4. Descrição: "Sistema web de gestão nutricional com ficha de anamnese digital"
5. Mantenha como Public ou Private
6. **NÃO** marque "Add README" (já temos um)
7. Clique em "Create repository"

### 2. Configurar Git Local

Abra o terminal na pasta do projeto e execute:

```bash
# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit: Sistema NutriSys - Fase 1 completa"

# Adicionar o repositório remoto (substitua SEU-USUARIO e nutrisys pelo seu)
git remote add origin https://github.com/SEU-USUARIO/nutrisys.git

# Enviar para o GitHub
git branch -M main
git push -u origin main
```

### 3. Estrutura do Repositório

Após o push, seu repositório terá:

```
nutrisys/
├── .gitignore              # Arquivos ignorados
├── LICENSE                 # Licença MIT
├── README.md               # Documentação principal
├── INSTALL.md              # Guia de instalação
├── ROADMAP.md              # Planejamento futuro
├── TEMPLATE_WORD_GUIDE.md  # Como criar templates
├── requirements.txt        # Dependências Python
├── manage.py               # Django CLI
├── setup.bat              # Setup Windows
├── setup.sh               # Setup Linux/Mac
├── nutri_system/          # Configurações Django
├── anamnese/              # App principal
├── media/                 # Arquivos gerados (ignorado no git)
└── db.sqlite3             # Banco de dados (ignorado no git)
```

## 🚀 Clonar em Outro Computador

Para usar em outra máquina:

```bash
# Clonar o repositório
git clone https://github.com/SEU-USUARIO/nutrisys.git

# Entrar na pasta
cd nutrisys

# Executar o setup
# Windows:
setup.bat
# Linux/Mac:
./setup.sh
```

## 🔄 Workflow de Desenvolvimento

### Fazer Alterações

```bash
# Ver o que mudou
git status

# Adicionar mudanças
git add .

# Fazer commit com mensagem descritiva
git commit -m "Adiciona cálculo de TMB"

# Enviar para o GitHub
git push
```

### Criar Features (Recomendado)

```bash
# Criar branch para nova funcionalidade
git checkout -b feature/calculos-nutricionais

# Trabalhar na feature...
# Fazer commits...

# Voltar para main
git checkout main

# Fazer merge da feature
git merge feature/calculos-nutricionais

# Enviar para o GitHub
git push
```

## 📝 Boas Práticas de Commit

Use mensagens claras e descritivas:

```bash
✅ Bom:
git commit -m "Adiciona validação de idade no formulário"
git commit -m "Corrige bug no cálculo de IMC"
git commit -m "Melhora layout da página de listagem"

❌ Ruim:
git commit -m "update"
git commit -m "fix"
git commit -m "changes"
```

### Padrão de Mensagens

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação, sem mudança de código
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Manutenção

Exemplos:
```bash
git commit -m "feat: adiciona cálculo de TMB e GET"
git commit -m "fix: corrige erro ao salvar ficha sem peso desejado"
git commit -m "docs: atualiza README com instruções de instalação"
```

## 🌟 README Atraente

O README.md já criado inclui:
- ✅ Badges de status
- ✅ Descrição clara
- ✅ Screenshots (você pode adicionar)
- ✅ Instruções de instalação
- ✅ Funcionalidades
- ✅ Roadmap
- ✅ Licença

### Adicionar Screenshots

1. Tire screenshots do sistema funcionando
2. Crie uma pasta `screenshots/`
3. Adicione as imagens
4. Referencie no README:

```markdown
## 📸 Screenshots

### Página Inicial
![Home](screenshots/home.png)

### Lista de Fichas
![Fichas](screenshots/lista.png)

### PDF Gerado
![PDF](screenshots/pdf.png)
```

## 🔒 Segurança

### O que NÃO deve ir para o GitHub

Já configurado no .gitignore:
- ❌ Banco de dados (db.sqlite3)
- ❌ Arquivos de mídia (PDFs gerados)
- ❌ Ambiente virtual (venv/)
- ❌ Arquivos de configuração local
- ❌ Senhas e chaves secretas

### Configuração em Produção

Para produção, crie um arquivo `.env`:

```bash
# .env (NÃO commite este arquivo!)
SECRET_KEY=sua-chave-super-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=seusite.com,www.seusite.com
DATABASE_URL=postgres://user:pass@host:5432/dbname
```

## 🌐 Deploy na Web (Opcional)

### Opções de Hosting

1. **Heroku** (Fácil, free tier disponível)
2. **PythonAnywhere** (Ideal para Django)
3. **DigitalOcean** (Mais controle)
4. **AWS** (Produção enterprise)
5. **Vercel/Netlify** (Frontend + Serverless backend)

### Deploy Rápido no Heroku

```bash
# Instalar Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Criar app
heroku create nutrisys-app

# Adicionar PostgreSQL
heroku addons:create heroku-postgresql:mini

# Deploy
git push heroku main

# Migrar banco
heroku run python manage.py migrate

# Criar superuser
heroku run python manage.py createsuperuser

# Abrir app
heroku open
```

## 📊 GitHub Actions (CI/CD)

Crie `.github/workflows/django.yml` para testes automáticos:

```yaml
name: Django CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test
```

## 🎯 Checklist antes do Push

- [ ] Código funciona localmente
- [ ] Nenhuma senha/chave no código
- [ ] .gitignore configurado
- [ ] README atualizado
- [ ] Commit com mensagem clara
- [ ] Removidos arquivos temporários

## 💡 Dicas Finais

1. **Commit frequentemente** - Melhor muitos commits pequenos que um grande
2. **Use branches** - Especialmente para features grandes
3. **Escreva README** - Ajuda você e outros desenvolvedores
4. **Documente mudanças** - Mantenha o ROADMAP.md atualizado
5. **Faça backup** - GitHub é seu backup, mas tenha backup local também

## 🆘 Comandos Úteis

```bash
# Ver histórico de commits
git log --oneline

# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1

# Desfazer mudanças em arquivo
git checkout -- arquivo.py

# Ver diferenças
git diff

# Atualizar do GitHub
git pull

# Ver branches
git branch

# Deletar branch
git branch -d nome-branch
```

## 📞 Precisa de Ajuda?

- Git: https://git-scm.com/doc
- GitHub: https://docs.github.com
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
