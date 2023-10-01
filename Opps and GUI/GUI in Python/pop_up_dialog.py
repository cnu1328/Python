from tkinter import *
from tkinter import messagebox

srinu = Tk()
def answer() :
    messagebox.showerror('Answer',"Sorry, no information recorded")

def callback() :
    if messagebox.askyesno('Verify', 'Really quit?'):
        messagebox.showwarning('Yes','Not yet implemented')
    else:
        messagebox.showinfo('No','Quit has been cancelled')

button = Button(srinu,text = 'Quit', command = callback)
button.pack(fill=X)
button = Button(srinu,text = 'Answer', command = answer)
button.pack(fill=X)


mainloop()
