# coding: utf-8

from ftplib import FTP, error_perm
from pathlib import Path

from colorama import Fore

from ftp_refresher.config import HOST, PASSWD, USER, FILENAMES, LOCAL_PATH


class RemoteClient:

    def __init__(self):
        # Adquire os dados das variáveis de ambiente
        self.host = HOST
        self.user = USER
        self.passwd = PASSWD
        self.local_path = Path(LOCAL_PATH)

    def execute(self):
        # Realiza a conexão com o servidor FTP
        ftp = FTP(HOST, USER, PASSWD)

        # Busca os arquivos que serão baixados
        for filename in FILENAMES:
            local_filename = self.local_path.joinpath(filename)
            # Salva os arquivos localmente
            with open(local_filename, 'wb') as file:
                try:
                    ftp.retrbinary(f'RETR {filename}', file.write)
                except error_perm:
                    print(f'{Fore.RED}Arquivo {filename!r} não encontrado!')
                    # Encerra a conexão com o arquivo e o deleta
                    file.close(), Path(file.name).unlink()
                    continue
            print(f'{Fore.GREEN}Arquivo {filename!r} baixado com sucesso!')

        # Fecha a conexão com o servidor
        ftp.abort()
