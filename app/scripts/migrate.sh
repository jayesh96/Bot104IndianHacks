#!/bin/sh

# First, makemigrations and migrate
echo "from django.contrib.auth.models import User; User.objects.filter(email='test@test.com').delete(); User.objects.create_superuser('test', 'test@test.com', 'pass1234')" | python manage.py shell
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate

# Now run the gunicorn server 
gunicorn --config /conf/gunicorn_config.py helloworld.wsgi
