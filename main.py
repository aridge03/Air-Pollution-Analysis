
import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main application window
app = tk.Tk()
app.title("Basic Tkinter App")

# Create a label widget
label = tk.Label(app, text="Welcome to Tkinter App")
label.pack(pady=10)

# Create a button widget
button = tk.Button(app, text="Click Me!", command=on_button_click)
button.pack(pady=5)

# Start the main even