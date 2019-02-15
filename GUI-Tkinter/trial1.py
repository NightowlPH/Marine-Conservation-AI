from tkinter import *
from tkinter import ttk
import tkinter as tk

HEIGHT = 300
WIDTH = 300

root = tk.Tk()
root.title('MWWP')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#
label = tk.Label(root, text="Choose image to classify")
label.place(anchor='n', relx=0.5, rely=0.1)

button = tk.Button(root, text="Import")
button.place(anchor='n', relx=0.5, rely=0.2)

# 
label = tk.Label(root, text="Begin the process")
label.place(anchor='s', relx=0.5, rely=0.4)

button = tk.Button(root, text="Start")
button.place(anchor='s', relx=0.5, rely=0.5)

# Output
frame = tk.Frame(root, bd=10)
frame.place(relx=0.5, rely=0.6, relwidth=0.90, relheight=0.4, anchor='n')

label = tk.Label(frame, bg='white')
label.place(relwidth=1, relheight=1)

root.resizable(False, False)
root.mainloop()