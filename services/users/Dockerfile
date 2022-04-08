# base image
FROM python:3.7.2-alpine

# Install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd && \
    apk add g++

# set working directory
WORKDIR /usr/src/app

# add and install requierements
COPY ./requierements.txt /usr/src/app/requierements.txt
RUN pip install -r requierements.txt

# add entrypoint.sh
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# RUN chmod 777 /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app/

# run server
CMD python manage.py run -h 0.0.0.0
# CMD ["/usr/src/app/entrypoint.sh"]
