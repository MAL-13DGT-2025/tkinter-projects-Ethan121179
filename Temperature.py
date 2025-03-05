import tkinter as tk 
from tkinter import ttk

def convert():

    result.config(text = f"{number.get()}")

root = tk.Tk()
con_var = tk.IntVar()

title = ttk.Label(root, text="Temperature\nConverter")
title.grid(row=0, column=0, columnspan= 2)

number = ttk.Entry(root)
number.grid(row = 1, column= 0, columnspan=2, padx=10, pady=10)

entry1 = ttk.Radiobutton(root, text="C to F", variable = con_var, value=1).grid(column=0, row=2, columnspan=1, padx=10, pady=10)
entry2 = ttk.Radiobutton(root, text="F to C", variable = con_var, value=2).grid(column=1, row=2, columnspan=1, padx=10, pady=10)

convert = ttk.Button(root, text = "Convert", command=convert)
convert.grid(row= 3, column= 0, columnspan=2, padx=10, pady=10)

result = ttk.Label(root, text = "")
result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)



root.mainloop()