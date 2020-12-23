# coding: utf-8

import tkinter as tk

from ftp_refresher.config import HOST, PASSWD, USER


class FTPGui:
    host: str = HOST
    user: str = USER
    passwd: str = PASSWD

    def __init__(self):
        self.gui = tk.Tk()

    def create_interface(self) -> None:
        # Insere o campo de inserção do endereço do servidor
        self.host = tk.Entry(self.gui)
        self.host.grid(row=0, column=1)
        tk.Label(self.gui, text='Host:').grid(row=0, pady=4)

        # Insere o campo de inserção do nome de usuário
        self.user = tk.Entry(self.gui)
        self.user.grid(row=1, column=1)
        tk.Label(self.gui, text='Usuário:').grid(row=1, pady=4)

        # Insere o campo de inserção da senha de acesso ao host
        self.passwd = tk.Entry(self.gui, show='*')
        self.passwd.grid(row=2, column=1)
        tk.Label(self.gui, text='Senha:').grid(row=2, pady=4)

        # Cria os botões de execução do script e saída da aplicação
        quit_bt = tk.Button(self.gui, text='Fechar', command=self.gui.quit)
        exec_bt = tk.Button(self.gui, text='Executar', command=self.get_data)

        # Posiciona os botões na interface
        exec_bt.grid(row=3, column=1, sticky=tk.W, pady=4)
        quit_bt.grid(row=3, column=0, sticky=tk.W, pady=4)

        self.gui.mainloop()

    def get_data(self) -> None:
        print(f'{self.host=} | {self.user=} | {self.passwd=}')
