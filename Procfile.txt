web: gunicorn setup.wsgi:application
release: python manage.py migrate
