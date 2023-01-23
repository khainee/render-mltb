from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror

QB_BASE_URL = environ.get('QB_BASE_URL', None)
try:
    if len(QB_BASE_URL) == 0:
        raise TypeError
    QB_BASE_URL = QB_BASE_URL.rstrip("/")
except TypeError:
    QB_BASE_URL = None
QB_SERVER_PORT = environ.get('QB_SERVER_PORT', None)
if QB_SERVER_PORT is not None and QB_BASE_URL is not None:
    while True:
        try:
            rget(QB_BASE_URL).status_code
            sleep(600)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
