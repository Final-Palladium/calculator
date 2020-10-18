def main():
    import tkinter as tk
    import styles
    from functions import calc_functions as funcs
#    from functions import auxiliary_functions as aux (temporarily deprecated)

    calc = tk.Tk()
    calc.title('Calc.py')
    calc['bg'] = styles.bg_color

    for i in range(9):
        bt = tk.Button(calc, text=i+1, bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg, command=lambda i=i+1: funcs.click(i))
        if i//3 == 0:
            bt.grid(row=0, column=i)
        elif i//6 == 0:
            bt.grid(row=1, column=i-3)
        else:
            bt.grid(row=2, column=i-6)
    for i in range(3):
        if i == 1:
            bt = tk.Button(calc, text=0, bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg, command=lambda i=0: funcs.click(i))
            bt.grid(row=3, column=1)
        else:
            bt = tk.Button(calc, text=" ", bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg)
            if i == 0:
                bt.grid(row=3, column=i)
            else:
                bt.grid(row=3, column=i)

    calc.mainloop()


if __name__ == "__main__":
    main()
