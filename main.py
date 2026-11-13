from tkinter import *
from tkinter import ttk

import json

start = Tk()

header = ttk.Frame(start, width=500, height=200, relief='sunken')
header.pack_propagate(False)

title = ttk.Label(header, text='Bem vindo(a)!\nEscolha uma opção para acessar o sistema:', justify='center')


sign = ttk.Frame(start, width=500, height=500, relief='sunken')
sign.grid_propagate(False)
sign.columnconfigure(0, weight=100)
sign.rowconfigure([0, 1, 2, 3, 4, 5, 6], pad=10, minsize=50)

sign_in = ttk.Button(sign, text='Entrar')
sign_up = ttk.Button(sign, text='Criar conta')

close = ttk.Button(sign, text='Fechar', command=start.destroy)

header.pack()
title.pack(expand=True)

sign.pack()
sign_in.grid(row=0, column=0)
sign_up.grid(row=1, column=0)
close.grid(row=3, column=0)


start.mainloop()
