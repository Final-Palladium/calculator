def main():
    import tkinter as tk
    import styles
    from functions import calc_functions as funcs

    calc = tk.Tk()
    calc.title('Calc.py')
    calc.resizable(0,0)
    calc['bg'] = styles.bg_color

    display = tk.Entry(calc, text='', font=styles.display_font, background=styles.bg_color, bd=0)
    display.grid(row=0, columnspan=5, pady=50)
    def click(i):
        display.delete(0, tk.END)
        display_text = funcs.click(i)
        display.insert(0, display_text)

    for i in range(9):
        bt = tk.Button(calc, text=str(i+1), bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font,
        height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg,
        activeforeground=styles.button_ac_fg, command=lambda i=str(i+1): click(i))
        if i//3 == 0:
            bt.grid(row=1, column=i)
        elif i//6 == 0:
            bt.grid(row=2, column=i-3)
        else:
            bt.grid(row=3, column=i-6)
    for i in range(3):
        if i == 1:
            bt = tk.Button(calc, text=str(0), bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font,
            height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg,
            activeforeground=styles.button_ac_fg, command=lambda i=str(0): click(i))
            bt.grid(row=4, column=1)
        else:
            bt = tk.Button(calc, text=styles.button_text[i+8], bd=styles.button_bd, bg=styles.button_bg, font=styles.button_font,
            height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg,
            activeforeground=styles.button_ac_fg, command=lambda i=styles.button_text[i+8]: click(i))
            if i == 0:
                bt.grid(row=4, column=i)
            else:
                bt.grid(row=4, column=i)
    for i in range(8):
        bt = tk.Button(calc, text=styles.button_text[i], bd=styles.button_bd, bg=styles.button_func_bg, font=styles.button_font,
        height=styles.button_height, width=styles.button_width, activebackground=styles.button_ac_bg,
        activeforeground=styles.button_ac_fg, command=lambda i=styles.button_text[i]: click(i))
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
