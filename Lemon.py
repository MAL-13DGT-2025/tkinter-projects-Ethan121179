import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Lemonade Stand")

# Frame for the input section
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

# Label and entry for lemonade quantity
quantity_label = ttk.Label(frame, text="How many lemonades would you like to order?")
quantity_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
lemonade_quantity_entry = ttk.Entry(frame)
lemonade_quantity_entry.grid(row=0, column=1, padx=5, pady=5)

# Add-on options (sugar and ice)
sugar_var = tk.BooleanVar()
ice_var = tk.BooleanVar()

# Sugar checkbox
sugar_check = ttk.Checkbutton(frame, text="Add sugar ($0.50)", variable=sugar_var)
sugar_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

# Ice checkbox
ice_check = ttk.Checkbutton(frame, text="Add ice ($0.30)", variable=ice_var)
ice_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)

# Button to calculate the total
calculate_button = ttk.Button(frame, text="Calculate Total")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to show the total cost (initially empty)
total_cost_label = ttk.Label(frame, text="Total Cost: $0.00")
total_cost_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
root.mainloop()
