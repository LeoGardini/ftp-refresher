# coding: utf-8

from time import time
from colorama import init, Fore, Style

from ftp_refresher.client import RemoteClient

if __name__ == '__main__':
    # Inicializa a coloração no terminal
    init(autoreset=True)

    # Informa o início do procedimento
    print(Fore.YELLOW + 'Iniciando transferência dos arquivos...\n')
    start = time()

    # Realiza a conexão FTP com o servidor e baixa os arquivos
    remote = RemoteClient()
    remote.execute()

    # Aguarda o usuário finalizar a aplicação
    execution = f'{Fore.GREEN}{Style.BRIGHT}{time() - start:.2f}{Fore.WHITE}'
    print(f'\nTransferência finalizada em {execution}s.')
    print(Fore.YELLOW + 'Aperte qualquer tecla para fechar...', end='')
    input()
