from tkinter import *
from tkinter import ttk

import json

start = Tk()

header = ttk.Frame(start, width=500, height=200, relief='sunken')
header.pack_propagate(True)

sign = ttk.Frame(start, width=500, height=500, relief='sunken')
sign.pack_propagate()

header.pack()
sign.pack()


start.mainloop()
