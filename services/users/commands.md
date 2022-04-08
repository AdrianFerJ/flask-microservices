# Basic commands to set up and run flask locally:
# ===============================================
``` bash
export FLASK_APP=project/__init__.py
export FLASK_ENV=development
python manage.py run
```


# Docker Commands:
# ================
```sh
# build
docker-compose build

# run and take down services
docker-compose up -d
docker-compose up -d --build
docker-compose down

# Logs
docker-compose logs

# Run tests
docker-compose exec users python manage.py test
```


# CURL Requests:
# ==============
``` bash
# Put
curl http://localhost:5000/ -d "data=some data" -X PUT

# Get
curl http://localhost:5001/users/ping

```

# Python's request:
# ==================
``` bash
# use flask sheel
flask shell

# or idlelib shell
python -m idlelib.idle
```

``` python
from requests import put, get

# Put
# put('http://localhost:5000/', data={'data': 'Remember the milk'}).json()

# Get
get('http://localhost:5001/users/ping').json()
```