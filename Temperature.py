import tkinter as tk 
from tkinter import ttk

def convert():
    num = int(number.get())
    
    if con_var.get() == 1: # Celsius to farenheit
        result = (num * 9/5) + 32
        result1.config(text = f"{num}C is equal to {round(result, 2)}F")
      
    elif con_var.get() ==2: # Farenheit to celsius
        result = (num - 32) * (5/9)
        result1.config(text = f"{num}F is equal to {round(result, 2)}C")
        

root = tk.Tk()
con_var = tk.IntVar(value=1)

title = ttk.Label(root, text="Temperature\nConverter")
title.grid(row=0, column=0, columnspan= 2)

number = ttk.Entry(root)
number.grid(row = 1, column= 0, columnspan=2, padx=10, pady=10)

entry1 = ttk.Radiobutton(root, text="C to F", variable = con_var, value=1)
entry1.grid(column=0, row=2)
entry2 = ttk.Radiobutton(root, text="F to C", variable = con_var, value=2)
entry2.grid(column=1, row=2)

convert = ttk.Button(root, text = "Convert", command=convert)
convert.grid(row= 3, column= 0, columnspan=2, padx=10, pady=10)

result1 = ttk.Label(root, text = "")
result1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()