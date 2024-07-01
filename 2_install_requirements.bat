SET MainDir=%~dp0
cd "%MainDir%"
call .\venv\Scripts\activate.bat
python -m pip install -r Project\requirements.txt
pause
pause