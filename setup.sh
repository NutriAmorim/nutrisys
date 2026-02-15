#!/bin/bash

echo "==================================="
echo "  NUTRISYS - Setup Rápido"
echo "==================================="
echo ""

echo "[1/6] Criando ambiente virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao criar ambiente virtual"
    exit 1
fi

echo "[2/6] Ativando ambiente virtual..."
source venv/bin/activate

echo "[3/6] Instalando dependências..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao instalar dependências"
    exit 1
fi

echo "[4/6] Configurando banco de dados..."
python manage.py makemigrations
python manage.py migrate

echo "[5/6] Criando diretórios de media..."
mkdir -p media/templates
mkdir -p media/pdfs
mkdir -p media/docs

echo ""
echo "==================================="
echo "  Instalação Concluída!"
echo "==================================="
echo ""
echo "Próximos passos:"
echo "1. Criar superusuário: python manage.py createsuperuser"
echo "2. Iniciar servidor: python manage.py runserver"
echo "3. Acessar: http://127.0.0.1:8000"
echo ""
read -p "Pressione ENTER para criar superusuário agora..."

echo ""
echo "[6/6] Criando superusuário..."
python manage.py createsuperuser

echo ""
read -p "Deseja iniciar o servidor agora? (s/n) " resposta
if [ "$resposta" = "s" ] || [ "$resposta" = "S" ]; then
    echo ""
    echo "Iniciando servidor..."
    echo "Acesse: http://127.0.0.1:8000"
    echo ""
    python manage.py runserver
fi
