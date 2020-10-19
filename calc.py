def main():
    import tkinter as tk
    import styles
    from functions import calc_functions as funcs
#    from functions import auxiliary_functions as aux (temporarily deprecated)

    calc = tk.Tk()
    calc.title('Calc.py')
    calc['bg'] = styles.bg_color

    display = tk.Label(calc, text='Display Text', font=styles.display_font, background=styles.bg_color, height=4)
    display.grid(row=0, columnspan=5)

    for i in range(9):
        bt = tk.Button(calc, text=str(i+1), bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg, command=lambda i=str(i+1): funcs.click(i))
        if i//3 == 0:
            bt.grid(row=1, column=i)
        elif i//6 == 0:
            bt.grid(row=2, column=i-3)
        else:
            bt.grid(row=3, column=i-6)
    for i in range(3):
        if i == 1:
            bt = tk.Button(calc, text=str(0), bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg, command=lambda i=str(0): funcs.click(i))
            bt.grid(row=4, column=1)
        else:
            bt = tk.Button(calc, text=styles.button_text[i+8], bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg, command=lambda i=styles.button_text[i+8]: funcs.click(i))
            if i == 0:
                bt.grid(row=4, column=i)
            else:
                bt.grid(row=4, column=i)
    for i in range(8):
        bt = tk.Button(calc, text=styles.button_text[i], bd=styles.button_bd, bg=styles.button_func_bg, font=styles.button_font, height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg, activeforeground=styles.button_ac_fg, command=lambda i=styles.button_text[i]: funcs.click(i))
        if i < 2:
            bt.grid(row=1, column=i+3)
        elif i < 4:
            bt.grid(row=2, column=i+1)
        elif i < 6:
            bt.grid(row=3, column=i-1)
        else:
            bt.grid(row=4, column=i-3)

    calc.mainloop()


if __name__ == "__main__":
    main()
