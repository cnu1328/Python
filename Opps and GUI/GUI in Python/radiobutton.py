from tkinter import *

def sel():
    selection = 'you selected the option '+ str( var.get())
    label.config(text= selection)

root = Tk()
var = IntVar()

r = Radiobutton(root, text = 'option1', variable = var, value = 1, command = sel)
r.pack(anchor = E)
r1 = Radiobutton(root,text = 'option2', variable = var, value = 2, command = sel)
r1.pack()
r2 = Radiobutton(root, text = 'option3', variable = var, value =3, command = sel)
r2.pack()

label = Label()
label.pack()

root.mainloop()
