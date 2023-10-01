from tkinter import *
import tkinter

srinu = Tk()

mb = Menubutton(srinu, text = "confidential", relief = RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff = 0)
mb['menu'] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label = 'mayo', variable = mayoVar)
mb.menu.add_checkbutton(label = 'Ketchup', variable = ketchVar)

mb.pack()
srinu.mainloop()
