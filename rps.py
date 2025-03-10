import tkinter as tk
from tkinter import ttk
import random

things = ["rock, paper, scissors"]

def choice(ting):
    comp_choice = random.randrange(0,3)
    if ting != things[comp_choice]:
        if ting == things[0] and comp_choice ==things[2] or ting ==[1] and comp_choice == things[0] or ting == things[2] and comp_choice == things[1]:
            tingels.config(text = f"You won, npc picked {things[comp_choice]}")
        else:
            tingels.config(text = f"You lost bozo, ncp picked{things[comp_choice]}")
    else:
        tingels.config(text = f"draw! select again bozo")
root = tk.Tk()
root.title("rockcok")

rps = ttk.Label(root, text = f'rock, paper/ siccor gayme')
rps.grid(column=1, row=0)

instructionss = ttk.Label(root, text = 'make your choicee')
instructionss.grid(column=1, row=1)

tingels = ttk.Label(root, text='')
tingels.grid(column=1, row=2)

rock = ttk.Button(root, text = 'rock', command= lambda : choice("rock"))
rock.grid(column=0, row= 3)

paper = ttk.Button(root, text = 'rock', command= lambda: choice("paper"))
paper.grid(column=1, row=3)

scissors = ttk.Button(root, text= 'sicrpos', command=lambda: choice("sceisors"))
scissors.grid(column=2, row=3)

root.mainloop()
