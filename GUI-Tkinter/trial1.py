from tkinter import *
from tkinter import ttk
import tkinter as tk

HEIGHT = 300
WIDTH = 300

root = tk.Tk()
root.title('MWWP')
label.wm_attributes('-alpha', 0.7)  

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#4197bd')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text="Choose image to classify")
label.pack()

button = tk.Button(frame, text="Import")
button.pack()

label = tk.Label(frame, text="Begin the process")
label.pack()

button = tk.Button(frame, text="Start")
button.pack()



root.resizable(False, False)
root.mainloop()