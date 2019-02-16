# Import libraries and functions
import tkinter as tk
from tkinter import *
from tkinter import ttk

from retrain import startRetrain
from test import startTest

HEIGHT = 300
WIDTH = 350

# Create Instance
windows = tk.Tk()

# Add a title to GUI
windows.title("Marine Animal Image Classifier")

frame = tk.Frame(windows)
frame.pack()

#set canvas size
canvas = tk.Canvas(windows, height=HEIGHT, width=WIDTH)
canvas.pack()

# Put "False" to make non-resizable
windows.resizable(True, True)

#tk.[widgetname](root window, properties/cofiguration)

#When Retrain button is clicked, retrain process starts
retrain_button = tk.Button(windows, text="Retrain", bg='#50a0d7', command=startRetrain)
retrain_button.place(anchor='s', relx=0.5, rely=0.1)

#when Test button is clicked, test process starts
test_button = tk.Button(windows, text="Test", bg='#50a0d7', command=startTest)
test_button.place(anchor='s', relx=0.5, rely=0.2)

# perform(tk, windows)

# Start the GUI/Create the main loop
windows.mainloop()