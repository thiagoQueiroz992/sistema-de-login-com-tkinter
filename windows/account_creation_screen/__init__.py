from tkinter import *
from tkinter import ttk

import json

def account_creation_screen() -> None:
    create_account = Tk()

    header = ttk.Frame(create_account, width=500, height=200, relief='sunken')
    header.pack_propagate(False)

    info = ttk.Frame(create_account, width=500, height=500, relief='sunken')
    info.pack_propagate(False)


    header.pack()
    info.pack()


    create_account.mainloop()