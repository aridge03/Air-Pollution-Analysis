
import tkinter as tk
from tkinter import ttk
import pandas as pd

def load_csv_data(file_path):
    # Read the CSV data using pandas
    return pd.read_csv(file_path)

def display_table():
    # Get the file path from the user (replace 'your_file.csv' with your actual file path)
    file_path = 'C:/Users/alyse.ridge/OneDrive - Government of Alberta/Documents/GitHub/Gui-Project-repo/first_40_lines.csv'

    # Load the CSV data into a pandas DataFrame
    data = load_csv_data(file_path)

    # Create a tkinter window
    root = tk.Tk()
    root.title("CSV Data Table")

    # Create a Treeview widget to display the table
    table = ttk.Treeview(root)

    # Configure columns
    columns = list(data.columns)
    table["columns"] = columns
    table.heading("#0", text="Index")
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    # Insert data into the table
    for index, row in data.iterrows():
        table.insert("", "end", text=index, values=list(row))

    # Pack the table and start the main event loop
    table.pack(expand=True, fill="both")
    root.mainloop()

def on_button_click():
    display_table()





if __name__ == "__main__":

  # Create the main application window
    app = tk.Tk()
    app.title("Button and Table Example")

    # Create a label widget
    label = tk.Label(app, text="Welcome to tkinter!")
    label.pack(pady=10)

    # Create a button widget
    button = tk.Button(app, text="Click Me!", command=on_button_click)
    button.pack(pady=10)

    # Start the main event loop
    app.mainloop()