import tkinter as tk
calc = tk.Tk()

def create_buttons():
    for i in range(9):
        bt = tk.Button(calc, text=i+1)
        if i//3 == 0:
            bt.grid(row=0, column=i)
        elif i//6 == 0:
            bt.grid(row=1, column=i-3)
        else:
            bt.grid(row=2, column=i-6)
    for i in range(3):
        if i == 1:
            bt = tk.Button(calc, text=0)
            bt.grid(row=3, column=1)
        else:
            bt = tk.Button(calc, text=" ")
            if i == 0:
                bt.grid(row=3, column=i)
            else:
                bt.grid(row=3, column=i)
