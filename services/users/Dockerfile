# base image
from python:3.7.2-alpine

# set working directory
WORKDIR /usr/src/app

# add and install requierements
COPY ./requierements.txt /usr/src/app/requierements.txt
RUN pip install -r requierements.txt

# add app
COPY . /usr/src/app/

# run server
CMD python manage.py run -h 0.0.0.0
