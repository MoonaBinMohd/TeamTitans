@echo off
setlocal
cd /d "%~dp0"

echo ========================================
echo Tunneling Claim Watch AI - One Command
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    pause
    exit /b 1
)

if not exist ".env" (
    if exist ".env.example" (
        copy /Y ".env.example" ".env" >nul
    )
)

python -c "import flask, flask_cors, dotenv, jwt, requests" >nul 2>&1
if errorlevel 1 (
    echo Installing required Python packages...
    pip install Flask==3.0.0 Flask-CORS==4.0.0 python-dotenv==1.0.0 PyJWT==2.8.0 requests==2.31.0
    if errorlevel 1 (
        echo Failed to install Python packages.
        pause
        exit /b 1
    )
)

echo Starting backend on http://localhost:5000 ...
start "ClaimWatch Backend" cmd /k "cd /d ""%~dp0"" && python main.py"

timeout /t 3 /nobreak >nul

echo Starting frontend on http://localhost:8000 ...
start "ClaimWatch Frontend" cmd /k "cd /d ""%~dp0"" && python -m http.server 8000"

timeout /t 2 /nobreak >nul

echo Opening website...
start "" "http://localhost:8000"

echo.
echo App started. Use these windows to stop servers when done.
echo.
