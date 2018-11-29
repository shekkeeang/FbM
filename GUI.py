import tkinter as tk
from tkinter import ttk
win = tk.Tk()

# Window Title
win.title("Python GUI")

# Control of window size
# Non resizable
win.resizable(0,0)

# Creating label
lLabel = ttk.Label(win, text="A Label")
lLabel.grid(column=0, row=0)

def bAction():
    bButton.configure(text="Hello")
#    lName = ttk.Label(win, text=getName.get())
#    lName.grid(column=1, row=0)

# Creating button
bButton = ttk.Button(win, text="Click OK", command=bAction)
bButton.grid(column=1, row=1)

# Creating text input box
getName = tk.StringVar()
txtName = ttk.Entry(win, width=12, textvariable=getName)
txtName.grid(column=0, row=1)

lName = ttk.Label(win, text=getName.get())
lName.grid(column=1, row=0)

win.mainloop()
