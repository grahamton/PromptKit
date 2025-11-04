# Dev test runner for PromptKit (PowerShell)
# Usage: from repo root, run: .\dev-test.ps1

param(
  [switch]$Recreate
)

Write-Host "PromptKit dev test runner" -ForegroundColor Cyan

$venv = Join-Path $PSScriptRoot ".venv"
if ($Recreate -and (Test-Path $venv)) {
  Write-Host "Removing existing venv..." -ForegroundColor Yellow
  Remove-Item -Recurse -Force $venv
}

if (-not (Test-Path $venv)) {
  Write-Host "Creating venv..." -ForegroundColor Yellow
  python -m venv $venv
}

$python = Join-Path $venv "Scripts/python.exe"
if (-not (Test-Path $python)) { Write-Error "Venv python not found"; exit 1 }

& $python -m pip install --upgrade pip

# Install webapp deps first (to avoid typer/fastapi-cli conflicts), then project w/o deps, then pytest
Write-Host "Installing webapp requirements..." -ForegroundColor Yellow
& $python -m pip install -r (Join-Path $PSScriptRoot 'webapp/requirements.txt')

Write-Host "Installing project (editable, no-deps) + pytest..." -ForegroundColor Yellow
& $python -m pip install -e .[dev] --no-deps
& $python -m pip install pytest==8.3.3

Write-Host "Running tests..." -ForegroundColor Yellow
& $python -m pytest

if ($LASTEXITCODE -eq 0) {
  Write-Host "All tests passed." -ForegroundColor Green
} else {
  Write-Host "Tests failed." -ForegroundColor Red
}

