# Import libraries
import tkinter as tk
from trial import perform

# Create Instance
windows = tk.Tk()

# Add a title to GUI
windows.title("Marine Animal Image Classifier")

#create frame
coolFrame = tk.Frame(windows) 

coolFrame.pack()

# Put "False" to make non-resizable
windows.resizable(False, False)

#tk.[widgetname](root window, properties/cofiguration)
# def perform():
#     tk.Label(windows, text="This is our first label").pack()

perform(tk, windows)

# Start the GUI/Create the main loop
windows.mainloop()