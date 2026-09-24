@echo off
chcp 65001 >nul
title Dashboard Indicadores - CESFAM Tongoy
cd /d "%~dp0"
echo ============================================================
echo   ACTUALIZAR DASHBOARD - Metas Sanitarias e IAAPS
echo   CESFAM Tongoy (105321) + PSR Guanaqueros (105405)
echo ============================================================
echo.
where python >nul 2>nul
if errorlevel 1 (
  echo [X] No se encontro Python. Instalelo desde https://www.python.org
  echo     y marque la casilla "Add Python to PATH" durante la instalacion.
  pause & exit /b 1
)
python -c "import openpyxl" 2>nul || (
  echo Instalando la libreria openpyxl por unica vez...
  python -m pip install openpyxl
)
set "CARPETA=%~dp0REM_2026"
if not exist "%CARPETA%" (
  echo [X] No existe la carpeta REM_2026 junto a este archivo.
  echo     Cree la carpeta y deje ahi los REM y el per capita.
  pause & exit /b 1
)
python actualizar_dashboard.py --carpeta "%CARPETA%"
if errorlevel 1 (
  echo.
  echo [X] La actualizacion se detuvo. Lea el mensaje de arriba.
  pause & exit /b 1
)
copy /y dashboard.html index.html >nul
echo.
echo [OK] Listo. Revise la pestana VALIDACION antes de publicar.
start "" "%~dp0dashboard.html"
pause
