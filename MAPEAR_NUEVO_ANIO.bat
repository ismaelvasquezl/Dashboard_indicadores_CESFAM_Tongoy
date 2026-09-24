@echo off
chcp 65001 >nul
title Mapear formulario REM de un anio nuevo - CESFAM Tongoy
cd /d "%~dp0"
echo ============================================================
echo   MAPEAR REM DE UN ANIO NUEVO
echo ============================================================
echo.
echo Use esto UNA vez al ano, cuando cambie el formulario REM.
echo Revisa donde quedo cada celda comparando las ETIQUETAS de
echo las filas con las del ano anterior, y propone los cambios.
echo NADA se aplica solo: usted revisa el informe antes de usarlo.
echo.
set /p ANIO="Escriba el ano nuevo (ej: 2027) y presione Enter: "
set /p BASE="Escriba el ano base a comparar (ej: 2026) y presione Enter: "
set "CARPETA=%~dp0REM_%ANIO%"
if not exist "%CARPETA%" (
  echo.
  echo [X] No existe la carpeta REM_%ANIO% junto a este archivo.
  echo     Cree la carpeta REM_%ANIO% y deje ahi los REM del ano nuevo.
  pause & exit /b 1
)
python mapear_rem.py --carpeta "%CARPETA%" --anio %ANIO% --base %BASE%
echo.
echo Revise arriba las filas marcadas como PROPUESTO o NO ENCONTRADA.
echo Si todo esta correcto, ya puede usar ACTUALIZAR.bat con el ano nuevo.
pause
