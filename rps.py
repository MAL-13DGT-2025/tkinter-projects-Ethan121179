import tkinter as tk
from tkinter import ttk
import random

# Corrected list of choices
things = ["rock", "paper", "scissors"]

def choice(ting):
    comp_choice = random.choice(things)
    if ting == comp_choice:
        tingels.config(text=f"Draw! NPC picked {comp_choice}")
    elif (ting == "rock" and comp_choice == "scissors") or \
         (ting == "paper" and comp_choice == "rock") or \
         (ting == "scissors" and comp_choice == "paper"):
        tingels.config(text=f"You won! NPC picked {comp_choice}")
    else:
        tingels.config(text=f"You lost! NPC picked {comp_choice}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Labels
rps = ttk.Label(root, text='Rock, Paper, Scissors Game')
rps.grid(column=1, row=0)

instructions = ttk.Label(root, text='Make your choice:')
instructions.grid(column=1, row=1)

tingels = ttk.Label(root, text='')
tingels.grid(column=1, row=2)

# Buttons
rock = ttk.Button(root, text='Rock', command=lambda: choice("rock"))
rock.grid(column=0, row=3)

paper = ttk.Button(root, text='Paper', command=lambda: choice("paper"))
paper.grid(column=1, row=3)

scissors = ttk.Button(root, text='Scissors', command=lambda: choice("scissors"))
scissors.grid(column=2, row=3)

# Run the Tkinter event loop
root.mainloop()