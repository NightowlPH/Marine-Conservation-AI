from tkinter import *
from tkinter import ttk
import tkinter as tk

HEIGHT = 300
WIDTH = 300

root = tk.Tk()
root.title('MWWP')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_label = tk.Label(root, bg='#41a2c6')
background_label.place(relwidth=1, relheight=1)

#
label = tk.Label(root, text="Choose image to classify", bg='#41a2c6')
label.place(anchor='n', relx=0.5, rely=0.1)

button = tk.Button(root, text="Import", bg='#50a0d7')
button.place(anchor='n', relx=0.5, rely=0.2)

# 
label = tk.Label(root, text="Begin the process", bg='#41a2c6')
label.place(anchor='s', relx=0.5, rely=0.4)

button = tk.Button(root, text="Start", bg='#50a0d7')
button.place(anchor='s', relx=0.5, rely=0.5)

# Output
frame = tk.Frame(root, bd=10, bg='#389bc0')
frame.place(relx=0.5, rely=0.55, relwidth=0.90, relheight=0.4, anchor='n')

label = tk.Label(frame, bg='white')
label.place(relwidth=1, relheight=1)

root.resizable(False, False)
root.mainloop()