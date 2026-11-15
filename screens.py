from tkinter import *
from tkinter import ttk

class Start():
    def __init__(self, window: Tk) -> None:
        self.__window = window

        self.header = ttk.Frame(self.__window, width=500, height=200, relief='sunken')
        self.sign = ttk.Frame(window, width=500, height=500, relief='sunken')

        self.title = ttk.Label(self.header, text='Bem vindo(a)!\nEscolha uma opção para acessar o sistema:', justify='center')
        self.sign_in = ttk.Button(self.sign, text='Entrar')
        self.sign_up = ttk.Button(self.sign, text='Criar conta')
        self.close = ttk.Button(self.sign, text='Fechar', command=self.__window.destroy)


        self.header.pack_propagate(False)
        self.sign.grid_propagate(False)
        self.sign.columnconfigure(0, weight=100)                         
        self.sign.rowconfigure([0, 1, 2, 3, 4, 5, 6], pad=10, minsize=50)
        
        self.__calling()

    def __calling(self) -> None:
        self.header.pack()
        self.sign.pack()

        self.title.pack()

        self.sign_in.grid(row=0, column=0)
        self.sign_up.grid(row=1, column=0)
        self.close.grid(row=3, column=0)
