FROM python:latest

LABEL MAINTAINER: 'joeliberal github'

ENV PYTHONNUNBUFFERED 1

RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

ADD requierment.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requierment.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir" , "blogpy", "--bind", ":8000", "blogpy.wsgi:application"]