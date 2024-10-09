@echo off
cd app
echo --------
echo Du kannst den Server nun unter folgender Adresse erreichen: http://127.0.0.1:8000/corona
echo --------
python manage.py runserver
pause