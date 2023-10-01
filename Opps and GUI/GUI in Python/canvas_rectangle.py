from tkinter import *

srinu = Tk()

s = Canvas(srinu,width=200,height=100)
s.pack()

s.create_rectangle(50, 20, 150, 80, fill= '#476042')
s.create_rectangle(65, 35, 135, 65, fill = 'yellow')

s.create_line(0,0,50,20, fill = '#476042',width=3)
s.create_line(0,100,50,80, fill = '#475942', width = 3)
s.create_line(150,20,200, 0, fill = '#476042', width = 3)
s.create_line(150, 80, 200, 100, fill = '#476042', width = 3)

mainloop()
