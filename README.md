# Sistema de Nutrição - Ficha de Anamnese

Sistema web para preenchimento de fichas de anamnese nutricional com geração automática de PDF.

## 🚀 Instalação

### Pré-requisitos
- Python 3.10 ou superior
- Git

### Passo a passo

1. **Clone o repositório**
```bash
git clone <seu-repositorio>
cd nutri_app
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Configure o banco de dados**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crie um superusuário (admin)**
```bash
python manage.py createsuperuser
```

7. **Rode o servidor**
```bash
python manage.py runserver
```

8. **Acesse o sistema**
- Abra o navegador em: http://localhost:8000
- Admin: http://localhost:8000/admin

## 📁 Estrutura do Projeto

```
nutri_app/
├── anamnese/              # App principal
│   ├── models.py         # Modelos de dados
│   ├── views.py          # Lógica das páginas
│   ├── forms.py          # Formulários
│   ├── urls.py           # Rotas
│   ├── utils.py          # Funções auxiliares (PDF, Word)
│   └── templates/        # Templates HTML
├── nutri_system/         # Configurações Django
├── media/                # Arquivos gerados (PDFs)
├── static/               # CSS, JS, imagens
└── templates/            # Templates base
```

## 🎯 Funcionalidades Implementadas

### Fase 1 (Atual)
- ✅ Formulário web para dados de anamnese
- ✅ Preenchimento automático de documento Word
- ✅ Geração de PDF da ficha
- ✅ Interface responsiva

### Fase 2 (Próxima)
- ⏳ Importação de dados do Excel (tabela TACO)
- ⏳ Cálculo de TMB e GET
- ⏳ Sistema de recordatório alimentar
- ⏳ Geração de plano alimentar personalizado

## 💡 Como Usar

1. **Adicionar Template Word**
   - Coloque sua ficha de anamnese (.docx) em `media/templates/ficha_anamnese_template.docx`
   - Use marcadores como `{{nome}}`, `{{idade}}`, `{{peso}}` no documento

2. **Preencher Ficha**
   - Acesse http://localhost:8000
   - Preencha o formulário
   - Clique em "Gerar Ficha"
   - O PDF será gerado automaticamente

3. **Visualizar Fichas Antigas**
   - Acesse http://localhost:8000/fichas
   - Veja todas as fichas já criadas
   - Baixe PDFs anteriores

## 🔧 Configurações

Edite `nutri_system/settings.py` para:
- Configurar banco de dados
- Ajustar diretório de media
- Configurar chave secreta

## 📦 Deploy

### GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <seu-repositorio>
git push -u origin main
```

### Heroku (exemplo)
```bash
heroku create nutri-app
git push heroku main
heroku run python manage.py migrate
```

## 🐛 Troubleshooting

**Erro ao gerar PDF:**
- Verifique se o template Word existe em `media/templates/`
- Confira os marcadores no documento Word

**Erro ao rodar servidor:**
- Ative o ambiente virtual
- Instale as dependências
- Execute as migrações

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no GitHub.
