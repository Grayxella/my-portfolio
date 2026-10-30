@echo off
cd /d "%~dp0"
echo Setting up your portfolio...
if not exist .venv (
  py -m venv .venv
  if errorlevel 1 python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo Installation failed. Check your internet connection and Python installation.
  pause
  exit /b 1
)
echo Starting your portfolio...
python app.py
pause
