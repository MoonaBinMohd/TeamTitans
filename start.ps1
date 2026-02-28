# Tunneling Claim Watch AI - Python Backend Startup Script
# For Windows PowerShell

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Tunneling Claim Watch AI" -ForegroundColor Cyan
Write-Host "Python Backend Startup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check Python version
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check if virtual environment exists
Write-Host ""
Write-Host "Checking virtual environment..." -ForegroundColor Yellow

if (Test-Path ".\venv") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Check if requirements are installed
Write-Host ""
Write-Host "Checking dependencies..." -ForegroundColor Yellow

$requirementsFile = "requirements.txt"
if (Test-Path $requirementsFile) {
    Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt -q
    Write-Host "✓ Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "⚠ requirements.txt not found" -ForegroundColor Yellow
}

# Check .env file
Write-Host ""
Write-Host "Checking environment configuration..." -ForegroundColor Yellow

if (Test-Path ".env") {
    Write-Host "✓ .env file found" -ForegroundColor Green
} else {
    if (Test-Path ".env.example") {
        Write-Host "Creating .env from .env.example..." -ForegroundColor Yellow
        Copy-Item ".env.example" ".env"
        Write-Host "✓ .env file created" -ForegroundColor Green
    } else {
        Write-Host "⚠ .env file not found, using defaults" -ForegroundColor Yellow
    }
}

# Show configuration
Write-Host ""
Write-Host "Configuration:" -ForegroundColor Cyan
Write-Host "  Backend URL: http://localhost:5000" -ForegroundColor Gray
Write-Host "  Frontend URL: http://localhost:8000" -ForegroundColor Gray
Write-Host "  API Docs: http://localhost:5000/" -ForegroundColor Gray

# Start the application
Write-Host ""
Write-Host "Starting application..." -ForegroundColor Yellow
Write-Host ""

python main.py
