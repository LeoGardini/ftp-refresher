# coding: utf-8

from os import environ

# Informações de acesso
HOST = environ.get('HOST')
USER = environ.get('USER')
PASSWD = environ.get('PASSWORD')

# Local onde serão armazenados os arquivos localmente
LOCAL_PATH = environ.get('LOCAL_PATH')

# Arquivos que serão baixados durante a execução
FILENAMES = [
    'SUBGRUPO.DBF', 'COD_KAR.NTX', 'DESC_KAR.NTX', 'COD_KAUX.NTX',
    'DATATEMP.DBF', 'KARDEX.DBF', 'KARDAUX.DBF', 'MINMAX.DBF', 'DESC_SUB.NTX',
    'COD_MMAX.NTX', 'COD_GRU.NTX', 'DESC_GRU.NTX', 'COD_SUB.NTX', 'GRUPOS.DBF'
]
