import tkinter as tk
from tkinter import ttk

def calculate_total():
    try:
        lemonade_quantity = int(lemonade_quantity_entry.get())
        lemonade_price = 2.00
        sugar_price = 0.50
        ice_price = 0.30
        sugar_choice = sugar_var.get()
        ice_choice = ice_var.get()
        total_cost = lemonade_quantity * lemonade_price
        if sugar_choice:
            total_cost += lemonade_quantity * sugar_price
        if ice_choice:
            total_cost += lemonade_quantity * ice_price
        total_cost_label.config(text=f"Total Cost: ${total_cost:.2f}")
    except ValueError:
        total_cost_label.config(text="Please enter a valid number for the quantity.")

root = tk.Tk()
root.title("Lemonade Stand")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_columnconfigure(0, weight=1)

header_frame = ttk.Frame(root, padding="10")
header_frame.grid(row=0, column=0, sticky="nsew")

header_label = ttk.Label(header_frame, text="Tu dalar lemons", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, padx=5, pady=10)

frame = ttk.Frame(root, padding="10")
frame.grid(row=1, column=0, sticky="nsew")

quantity_label = ttk.Label(frame, text="How many lemonades would you like to order?")
quantity_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
lemonade_quantity_entry = ttk.Entry(frame)
lemonade_quantity_entry.grid(row=0, column=1, padx=5, pady=5)

sugar_var = tk.BooleanVar()
ice_var = tk.BooleanVar()

sugar_check = ttk.Checkbutton(frame, text="Add sugar ($0.50)", variable=sugar_var)
sugar_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

ice_check = ttk.Checkbutton(frame, text="Add ice ($0.30)", variable=ice_var)
ice_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

total_cost_label = ttk.Label(frame, text="Total Cost: $0.00")
total_cost_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
