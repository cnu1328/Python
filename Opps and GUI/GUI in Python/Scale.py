from tkinter import *

def sel():
    selection = "Value : " + str(var.get())
    label.config(text = selection)

srinu = Tk()
var = DoubleVar()

scale = Scale(srinu, variable = var)
scale.pack(anchor = CENTER)

botton = Button(srinu, text = "Get scale value", command = sel)
botton.pack(anchor = CENTER)

label = Label(srinu)

label.pack()
srinu.mainloop()
