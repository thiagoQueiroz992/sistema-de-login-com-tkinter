import tkinter
import json

start_screen = tkinter.Tk()
header = tkinter.Frame(start_screen, background="gray", width=500, height=150)
sign = tkinter.Frame(start_screen, background="yellow", width=500, height=300)

title = tkinter.Label(header, text="Bem-vindo!\nEscolha uma opção:")

header.pack()
sign.pack()
header.pack_propagate(False)
sign.pack_propagate(False)

title.pack()

start_screen.mainloop()
