@echo off
echo Starte PMG-Webscrapper...
echo.

:: Wechselt in den src-Ordner und startet main.py mit dem Python aus der .venv
call .venv\Scripts\activate
python src\main.py

echo.
echo Bot-Durchlauf beendet.
pause