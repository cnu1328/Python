from tkinter import *

srinu = Tk()

canvas_width = 500
canvas_height = 250

w = Canvas(srinu,
           width=canvas_width,
           height=canvas_height)

w.pack()

y = int(canvas_height/2)

w.create_line(0,y,canvas_width,y,fill = '#470642')

srinu.mainloop()
