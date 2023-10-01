from tkinter import *

srinu = Tk()

frame = Frame(srinu)
frame.pack()

bottomframe = Frame(srinu)
bottomframe.pack( side = BOTTOM)

redbutton = Button(frame, text = "Red", fg = 'red')
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Green", fg = 'green')
greenbutton.pack( side = LEFT)

bluebotton = Button(frame, text = "Blue", fg = 'blue')
bluebotton.pack(side = LEFT)

blackbotton = Button(bottomframe, text = "Black", fg = 'black')
blackbotton.pack( side = BOTTOM)

srinu.mainloop()
