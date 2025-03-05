import tkinter as tk
from tkinter import ttk



root = tk.Tk()

number = ttk.Entry(root)
number.grid(row = 0, column= 0, columnspan=4)

entry1 = ttk.Button(root, text="7")
entry1.grid(column=0, row=1)
entry2 = ttk.Button(root, text="8")
entry2.grid(column=1, row=1)
entry3 = ttk.Button(root, text="9")
entry3.grid(column=2, row=1)
entry4 = ttk.Button(root, text="/")
entry4.grid(column=3, row=1)
entry5 = ttk.Button(root, text="4")
entry5.grid(column=0, row=2)
entry6 = ttk.Button(root, text="5")
entry6.grid(column=1, row=2)
entry7 = ttk.Button(root, text="6")
entry7.grid(column=2, row=2)
entry8 = ttk.Button(root, text="*")
entry8.grid(column=3, row=2)
entry9 = ttk.Button(root, text="1")
entry9.grid(column=0, row=3)
entry10 = ttk.Button(root, text="2")
entry10.grid(column=1, row=3)
entry11 = ttk.Button(root, text="3")
entry11.grid(column=2, row=3)
entry12 = ttk.Button(root, text="-")
entry12.grid(column=3, row=3)
entry13 = ttk.Button(root, text="CRL")
entry13.grid(column=0, row=4)
entry14 = ttk.Button(root, text="0")
entry14.grid(column=1, row=4)
entry15 = ttk.Button(root, text="=")
entry15.grid(column=2, row=4)
entry16 = ttk.Button(root, text="+")
entry16.grid(column=3, row=4)

root.mainloop()