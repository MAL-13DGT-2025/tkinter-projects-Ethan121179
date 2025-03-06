import tkinter as tk
from tkinter import ttk

def on_button_click(balyu):
    current = equation.get()
    current = current + balyu
    print(current)
    equation.set(current)

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(number.get())
        equation.set(result)
    except:
        equation.set("Error lol")
 
root = tk.Tk()
root.title("Calculator")

equation = tk.StringVar()

number = ttk.Entry(root, textvariable= equation)
number.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=90)

entry1 = ttk.Button(root, text="7", command=lambda: on_button_click("7"))
entry1.grid(column=0, row=1)
entry2 = ttk.Button(root, text="8", command=lambda: on_button_click("8"))
entry2.grid(column=1, row=1)
entry3 = ttk.Button(root, text="9", command=lambda: on_button_click("9"))
entry3.grid(column=2, row=1)
entry4 = ttk.Button(root, text="/", command=lambda: on_button_click("/"))
entry4.grid(column=3, row=1)
entry5 = ttk.Button(root, text="4", command=lambda: on_button_click("4"))
entry5.grid(column=0, row=2)
entry6 = ttk.Button(root, text="5", command=lambda: on_button_click("5"))
entry6.grid(column=1, row=2)
entry7 = ttk.Button(root, text="6", command=lambda: on_button_click("6"))
entry7.grid(column=2, row=2)
entry8 = ttk.Button(root, text="*", command=lambda: on_button_click("*"))
entry8.grid(column=3, row=2)
entry9 = ttk.Button(root, text="1", command=lambda: on_button_click("1"))
entry9.grid(column=0, row=3)
entry10 = ttk.Button(root, text="2", command=lambda: on_button_click("2"))
entry10.grid(column=1, row=3)
entry11 = ttk.Button(root, text="3", command=lambda: on_button_click("3"))
entry11.grid(column=2, row=3)
entry12 = ttk.Button(root, text="-", command=lambda: on_button_click("-"))
entry12.grid(column=3, row=3)
entry13 = ttk.Button(root, text="CRL", command=clear)
entry13.grid(column=0, row=4)
entry14 = ttk.Button(root, text="0", command=lambda: on_button_click("0"))
entry14.grid(column=1, row=4)
entry15 = ttk.Button(root, text="=", command=calculate)
entry15.grid(column=2, row=4)
entry16 = ttk.Button(root, text="+", command=lambda: on_button_click("+"))
entry16.grid(column=3, row=4)

root.mainloop()
