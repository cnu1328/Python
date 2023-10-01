from tkinter import *

srinu = Tk()

scrollbar = Scrollbar(srinu)

scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(srinu, yscrollcommand = scrollbar.set)

for line in range(100):
    mylist.insert(END, "This is count : " + str(line))

mylist.pack(side = LEFT, fill = BOTH)

scrollbar.config(command = mylist.yview)

mainloop()
