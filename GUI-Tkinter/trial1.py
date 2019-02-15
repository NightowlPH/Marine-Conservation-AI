from tkinter import *
from tkinter import ttk
import tkinter as tk

HEIGHT = 300
WIDTH = 350

def import_function():
    print("Import button clicked!")

def start_function():
    print("Start button clicked!")


# Main window
root = tk.Tk()
root.title('Marine Animal Image Classifier')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_label = tk.Label(root, bg='#41a2c6')
background_label.place(relwidth=1, relheight=1)


# Importing data images
# label = tk.Label(root, text="Choose image to classify", fg='white', bg='#41a2c6')
label = tk.Label(root, text="Choose image to classify", bg='#41a2c6')
label.place(anchor='n', relx=0.5, rely=0.1)

button = tk.Button(root, text="Import", bg='#50a0d7', command=import_function)
button.place(anchor='n', relx=0.5, rely=0.2)

# Start 
label = tk.Label(root, text="Begin the process", bg='#41a2c6')
label.place(anchor='s', relx=0.5, rely=0.4)

# button = tk.Button(root, text="Start", bg='#50a0d7', command=lambda: action())
button = tk.Button(root, text="Start", bg='#50a0d7', command=start_function)
button.place(anchor='s', relx=0.5, rely=0.5)

# Output - display the results 
frame = tk.Frame(root, bd=10, bg='#389bc0')
frame.place(relx=0.5, rely=0.55, relwidth=0.90, relheight=0.4, anchor='n')

label = tk.Label(frame, bg='white')
label.place(relwidth=1, relheight=1)



root.resizable(False, False)
root.mainloop()