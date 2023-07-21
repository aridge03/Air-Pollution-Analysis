
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    # Read CSV data (replace 'data.csv' with your actual file path)
    df = pd.read_csv('first_40_lines.csv')

    # Plot the graph using matplotlib
    fig, ax = plt.subplots()
    ax.plot(df['X'], df['Y'], marker='o', linestyle='-')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_title('CSV Data Plot')

    # Display the graph on the tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main application window
root = tk.Tk()
root.title("CSV Data Graph")

# Button to plot the graph
plot_button = tk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.pack(pady=10)

# Start the main event loop
root.mainloop()

