# coding: utf-8

import colorama

from ftp_refresher.client import RemoteClient

if __name__ == '__main__':
    # Inicializa a coloração no terminal
    colorama.init(autoreset=True)

    # Realiza a conexão FTP com o servidor e baixa os arquivos
    remote = RemoteClient()
    remote.execute()
