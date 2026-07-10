@echo off
echo 🚀 Flight Delay Predictor - Starting Application...
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo Please run setup first: python setup.py
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if streamlit is installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ❌ Streamlit not found! Installing dependencies...
    pip install -r requirements.txt
)

REM Run the application
echo 🚀 Starting Flight Delay Predictor...
echo 📱 Application will open in your browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run app.py --server.port 8501

pause 