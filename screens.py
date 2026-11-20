from tkinter import *
from tkinter import ttk

class Screen:
    def __init__(self, window: Tk) -> None:
        self._window = window

        self.header = ttk.Frame(self._window, width=500, height=200, relief='sunken')
        self.body = ttk.Frame(self._window, width=500, height=500, relief='sunken')

        self.header.pack_propagate(False)
        self.body.grid_propagate(False)

        self.body.columnconfigure(0, weight=100)
        self.body.rowconfigure([0, 1, 2, 3, 4, 5, 6], pad=10, minsize=50)

    def _calling(self) -> None:
        self.header.pack()
        self.body.pack()

    def change_screen(self, screen: "Screen") -> None:
        for widget in self._window.winfo_children():
            widget.destroy()

        screen(self._window)


class Start(Screen):
    def __init__(self, window: Tk) -> None:
        super().__init__(window)

        self.title = ttk.Label(self.header, text='Bem vindo(a)!\nEscolha uma opção para acessar o sistema:', justify='center')
        self.sign_in = ttk.Button(self.body, text='Entrar')
        self.sign_up = ttk.Button(self.body, text='Criar conta', command=lambda: self.change_screen(CreateAccount))
        self.close = ttk.Button(self.body, text='Fechar', command=self._window.destroy)

        self._calling()

    def _calling(self) -> None:
        super()._calling()

        self.title.pack()

        self.sign_in.grid(row=0, column=0)
        self.sign_up.grid(row=1, column=0)
        self.close.grid(row=3, column=0)


class CreateAccount(Screen):
    def __init__(self, window: Tk) -> None:
        super().__init__(window)

        self.title = ttk.Label(self.header, text='Insira seus dados para criação da conta.')
        
        self.name = ttk.Labelframe(self.body, text='Nome')
        self.lastname = ttk.Labelframe(self.body, text='Sobrenome')
        self.username = ttk.Labelframe(self.body, text='Nome de usuário')
        self.password = ttk.Labelframe(self.body, text='Senha')
        self.confpassword = ttk.Labelframe(self.body, text='Confirmar senha')

        self.entry_name = ttk.Entry(self.name, width=50)
        self.entry_lastname = ttk.Entry(self.lastname, width=50)
        self.entry_username = ttk.Entry(self.username, width=50)
        self.entry_password = ttk.Entry(self.password, width=50)
        self.entry_confpassword = ttk.Entry(self.confpassword, width=50)

        self._calling()

    def _calling(self) -> None:
        super()._calling()

        self.title.pack()
        self.name.grid(row=0, column=0)
        self.lastname.grid(row=1, column=0)
        self.username.grid(row=3, column=0)
        self.password.grid(row=4, column=0)
        self.confpassword.grid(row=5, column=0)

        self.entry_name.pack()
        self.entry_lastname.pack()
        self.entry_username.pack()
        self.entry_password.pack()
        self.entry_confpassword.pack()
