@echo off
echo === Instalador da Plataforma de Dieta — Vovô Fabio ===
echo.
cd /d "%~dp0"

REM Verifica se Python está disponível
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado. Instale o Python 3.10+ em https://python.org
    pause
    exit /b 1
)

echo Criando ambiente virtual...
python -m venv .venv

echo Instalando dependencias...
.venv\Scripts\python.exe -m pip install --upgrade pip --quiet
.venv\Scripts\python.exe -m pip install customtkinter Pillow

echo.
echo === Instalacao concluida! ===
echo Para iniciar o aplicativo, clique duas vezes em: iniciar.bat
echo.
pause
