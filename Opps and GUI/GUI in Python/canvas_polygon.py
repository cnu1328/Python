from tkinter import *

canvas_width = 200
canvas_height = 200
python_green = '#476042'

srinu = Tk()

s = Canvas(srinu,
           width = canvas_width,
           height = canvas_height)

s.pack()

points = [100,140,110,110,140,100,110,90,100,60,90,90,60,100,90,100]

s.create_polygon(points, outline = python_green,
                 fill = 'yellow', width = 3)

srinu.mainloop()
