@echo off
echo Iniciando Plataforma de Dieta — Vovô Fabio...
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    .venv\Scripts\python.exe main.py
) else (
    python main.py
)
