@echo off
pip install -r requirements.txt
cd app
python manage.py migrate
python manage.py makemigrations
pause
