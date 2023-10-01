import tkinter as tk
from tkinter import filedialog
import os

application_window = tk.Tk()

# Build a list of tples for each file type the file dialog should display

my_filetypes = [('all files', '.*'), ('text files', '.txt')]

#Ask the user to select a folder.

answer = filedialog.askdirectory(parent = application_window,
                                 initialdir=os.getcwd(),
                                 title = 'Please select a file : ')

#Ask the user to select a single file
answer = filedialog.askopenfilename(parent = application_window,
                                 initialdir = os.getcwd(),
                                 title = 'Please select a file',
                                 filetypes = my_filetypes)

#Ask the user to select multiple files
answer = filedialog.askopenfilenames(parent = application_window,
                                 initialdir = os.getcwd(),
                                 title = 'please select multiple files',
                                 filetypes = my_filetypes)
#Ask the user to save the file
answer = filedialog.asksaveasfilename(parent = application_window,
                                      initialdir = os.getcwd(),
                                      title = 'Please select the file name to save : ',
                                      filetypes = my_filetypes)
