import tkinter as tk
import tkinter.ttk as ttk

# Alternative (this way it uses themed - ttk - when available, with fallback standard/legacy ones if there is no alternative:
# from tkinter import *
# from tkinter.ttk import *


window = tk.Tk()

# greeting = tk.Label("Well, hello there!")
greeting = ttk.Label(window, text = "Well, hello there!")

greeting.pack()

# runs the app, awaiting events:
window.mainloop()