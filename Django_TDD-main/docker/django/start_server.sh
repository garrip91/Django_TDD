python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn --workers=3 --bind=0.0.0.0:8000 DJANGO_TDD_Project.wsgi:application