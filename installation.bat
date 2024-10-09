@echo off
cd app
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
pause