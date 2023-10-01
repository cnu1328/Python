from tkinter import *

root = Tk()

text = Text(root)

text.insert(INSERT,"Hello....World..")
text.insert(END,"How are you.?")

text.pack()

text.tag_add("here","1.0","1.7")
text.tag_add("start","1.8","1.26")
text.tag_config("here", background = "yellow", foreground= "blue")
text.tag_config("start", background= "orange", foreground = "green")

root.mainloop()

