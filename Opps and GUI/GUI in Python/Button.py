from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry('200x200')

def helloCallBack() :
    msg = messagebox.showinfo('Hello Python', 'Hello World')

B = Button(top, text = 'Hello', command = helloCallBack)

B.place(x= 10, y = 10)

top.mainloop()
