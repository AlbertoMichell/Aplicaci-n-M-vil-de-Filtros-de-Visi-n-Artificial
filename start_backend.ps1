# Script para iniciar el backend
# Ejecutar desde la carpeta raiz del proyecto

Write-Host "Iniciando servidor backend..." -ForegroundColor Green

# Navegar a la carpeta backend
Set-Location backend

# Verificar si Python esta instalado
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python no esta instalado" -ForegroundColor Red
    exit 1
}

# Verificar si las dependencias estan instaladas
Write-Host "Verificando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

# Iniciar servidor
Write-Host "Iniciando servidor en http://0.0.0.0:8001" -ForegroundColor Green
Write-Host "Documentacion disponible en http://localhost:8001/docs" -ForegroundColor Cyan
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Yellow

python main.py
