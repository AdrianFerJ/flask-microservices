# Comands:
# ===========
"""
export FLASK_APP=project/__init__.py
export FLASK_ENV=development
python manage.py run
"""


# CURL:
# =====
'''
# Put
curl http://localhost:5000/ -d "data=some data" -X PUT

# Get
curl http://localhost:5000/
'''

# Python's request
#=================
from requests import put, get

# Put
# put('http://localhost:5000/', data={'data': 'Remember the milk'}).json()

# Get
get('http://localhost:5000/users/ping').json()
