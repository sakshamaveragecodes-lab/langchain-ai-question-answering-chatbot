@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    py -m venv .venv
    if errorlevel 1 goto :error
)

call ".venv\Scripts\activate.bat"

echo Installing/updating required packages...
python -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo.
echo Starting PyMentor AI...
python app.py
set EXITCODE=%ERRORLEVEL%

echo.
pause
exit /b %EXITCODE%

:error
echo.
echo Setup failed. Make sure Python 3.10 or newer and internet access are available.
pause
exit /b 1
