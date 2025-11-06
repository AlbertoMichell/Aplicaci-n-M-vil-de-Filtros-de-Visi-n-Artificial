# Script de despliegue automático en Railway
# Autor: Mich
# Fecha: 4 de noviembre de 2025

Write-Host "=== Despliegue de Backend en Railway ===" -ForegroundColor Cyan
Write-Host ""

# Verificar Railway CLI
Write-Host "1. Verificando Railway CLI..." -ForegroundColor Yellow
try {
    $railwayVersion = railway --version 2>&1
    Write-Host "   Railway CLI instalado: $railwayVersion" -ForegroundColor Green
} catch {
    Write-Host "   Error: Railway CLI no encontrado" -ForegroundColor Red
    Write-Host "   Instalar con: npm install -g @railway/cli" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "2. Preparando para login..." -ForegroundColor Yellow
Write-Host "   Se abrirá tu navegador para autenticarte" -ForegroundColor Gray
Write-Host "   Usuario sugerido: Mich" -ForegroundColor Gray
Write-Host ""
Read-Host "   Presiona Enter para continuar"

# Login en Railway
Set-Location "D:\Appmovil\backend"
railway login

if ($LASTEXITCODE -ne 0) {
    Write-Host "   Error en login" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "3. Creando proyecto en Railway..." -ForegroundColor Yellow
Write-Host "   Nombre del proyecto: filtros-vision-mich" -ForegroundColor Gray

# Inicializar proyecto
railway init --name "filtros-vision-mich" 2>&1

Write-Host ""
Write-Host "4. Desplegando backend..." -ForegroundColor Yellow
Write-Host "   Esto puede tardar 2-3 minutos..." -ForegroundColor Gray
Write-Host ""

# Desplegar
railway up

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "   Error en despliegue" -ForegroundColor Red
    Write-Host "   Revisa los logs en: https://railway.app/dashboard" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "5. Generando dominio público..." -ForegroundColor Yellow

# Generar dominio
$domain = railway domain 2>&1

Write-Host ""
Write-Host "=== Despliegue completado ===" -ForegroundColor Green
Write-Host ""
Write-Host "URL del backend:" -ForegroundColor Cyan
Write-Host "https://$domain" -ForegroundColor White
Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor Yellow
Write-Host "1. Verificar que funciona:" -ForegroundColor Gray
Write-Host "   curl https://$domain/health" -ForegroundColor White
Write-Host ""
Write-Host "2. Actualizar Flutter:" -ForegroundColor Gray
Write-Host "   Editar: D:\Appmovil\lib\services\image_processing_service.dart" -ForegroundColor White
Write-Host "   Cambiar baseUrl a: https://$domain" -ForegroundColor White
Write-Host ""
Write-Host "3. Recompilar APK:" -ForegroundColor Gray
Write-Host "   flutter build apk --release" -ForegroundColor White
Write-Host ""
Write-Host "Dashboard de Railway: https://railway.app/dashboard" -ForegroundColor Cyan
Write-Host ""
