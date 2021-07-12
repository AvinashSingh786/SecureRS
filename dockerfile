FROM python:3.7

ADD . /SecureRS

WORKDIR /SecureRS

RUN pip3 install -r requirements.txt
CMD [ "python", "manage.py", "makemigrations", "home" ]
CMD [ "python", "manage.py", "migrate" ]
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
CMD [ "python", "manage.py", "runsslserver", "0.0.0.0:443" ]

EXPOSE 443/tcp

MAINTAINER Avinash tashan.avi@gmail.com