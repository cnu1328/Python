from tkinter import *
from tkinter import colorchooser

def callback() :
    result = colorchooser.askcolor(color = '#6A9662',
                                   title = "Bernd's Colour Chooser")
    print(result)

srinu = Tk()

Button(srinu,
       text = 'Choose Color',
       fg = 'darkgreen',
       command = callback).pack(side = LEFT, padx =10)
Button(text = 'Quit',
       command = srinu.quit,
       fg = 'red').pack(side = LEFT, padx =10)

mainloop()
       
