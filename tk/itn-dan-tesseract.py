import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

#Function to generate random points and plot them
def plot_random_points():
    # Number of points to generate
    number_of_points = 100
    # Generate random points
    x = [random.uniform(-10, 10) for _ in range(number_of_points)]
    y = [random.uniform(-10, 10) for _ in range(number_of_points)]

    # Clear previous figure
    a.cla()
    # Plot random points
    a.scatter(x, y)
    # Draw the plot
    canvas.draw()

#Create main window
root = tk.Tk()
root.title("Random Points Plotter")

#Create a tkinter Frame for the buttons
frame = ttk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.BOTH)

#Button to plot random points
plot_button = ttk.Button(frame, text="Plot Random Points", command=plot_random_points)
plot_button.pack(side=tk.LEFT)

#Set up the matplotlib figure and axes
fig = Figure(figsize=(5, 4), dpi=100)
a = fig.add_subplot(111)

#Create a canvas to embed the matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#Start the Tkinter event loop
root.mainloop()