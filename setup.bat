@echo off
echo ===================================
echo   NUTRISYS - Setup Rapido
echo ===================================
echo.

echo [1/6] Criando ambiente virtual...
python -m venv venv
if errorlevel 1 (
    echo ERRO: Falha ao criar ambiente virtual
    pause
    exit /b 1
)

echo [2/6] Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo [3/6] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERRO: Falha ao instalar dependencias
    pause
    exit /b 1
)

echo [4/6] Configurando banco de dados...
python manage.py makemigrations
python manage.py migrate

echo [5/6] Criando diretorios de media...
if not exist "media\templates" mkdir media\templates
if not exist "media\pdfs" mkdir media\pdfs
if not exist "media\docs" mkdir media\docs

echo.
echo ===================================
echo   Instalacao Concluida!
echo ===================================
echo.
echo Proximos passos:
echo 1. Criar superusuario: python manage.py createsuperuser
echo 2. Iniciar servidor: python manage.py runserver
echo 3. Acessar: http://127.0.0.1:8000
echo.
echo Pressione qualquer tecla para criar superusuario agora...
pause > nul

echo.
echo [6/6] Criando superusuario...
python manage.py createsuperuser

echo.
echo ===================================
echo Deseja iniciar o servidor agora? (S/N)
set /p resposta=
if /i "%resposta%"=="S" (
    echo.
    echo Iniciando servidor...
    echo Acesse: http://127.0.0.1:8000
    echo.
    python manage.py runserver
)

pause
