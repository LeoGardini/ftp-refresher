# coding: utf-8

import json
from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path.cwd().joinpath('.env'))

# Informações de acesso
HOST = environ.get('HOST')
USER = environ.get('USER')
PASSWD = environ.get('PASSWORD')

# Local onde serão armazenados os arquivos localmente
LOCAL_PATH = environ.get('LOCAL_PATH')

# Arquivos que serão baixados durante a execução
FILENAMES = json.loads(environ.get('FILENAMES'))
