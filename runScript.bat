@echo off

echo setting up virtual environment, this may take a upto 3 minutes...

:: Step 1: Run 'venv' to create a virtual environment in the same folder
python -m venv ve
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    pause
    exit /b
)

:: Step 3: Activate the virtual environment
call ve\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b
)

:: Step 4: Install packages from requirements.txt
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install packages from requirements.txt.
    pause
    exit /b
)

:: Step 5: Run main.py and input_data.txt
cls
call start notepad "input_data.txt" && python main.py