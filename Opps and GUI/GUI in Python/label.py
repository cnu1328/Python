from tkinter import *

root = Tk()

root.geometry('200x200')

var = StringVar()

label = Label(root, textvariable = var, )
var.set('Hey!! Here i\'m using Python')


label.pack()
root.mainloop()
