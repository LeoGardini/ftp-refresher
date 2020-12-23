# coding: utf-8

from os import environ, path

from dotenv import load_dotenv

# Carrega as informações do .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Informações de acesso
HOST = environ.get('HOST')
USER = environ.get('USER')
PASSWD = environ.get('PASSWORD')
SSH_KEY = environ.get('SSH_KEY')
REMOTE_PATH = environ.get('REMOTE_PATH')
