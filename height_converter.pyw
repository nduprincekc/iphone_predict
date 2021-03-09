import tkinter
from tkinter import DoubleVar, Button, Tk, Label, Entry,END

window = Tk()
window.title('Feet to Meter Conversion app')
window.config(background='blue')
window.geometry('320x220')
window.resizable(width=False, height=False)


def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set('%.4f' % meter)

def clea():
   # ft_entry.delete(0, tk.END)
    ft_entry.delete(0,END)
    mt_entry.delete(0,END)
ft_lbl = Label(window, text='FEET', bg='purple', fg='white', width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
# ft_entry.delete(0,'end')

mt_lbl = Label(window, text='meter', bg='red', fg='white', width=14)
mt_lbl.grid(column=0, row=1)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0,'end')


# creating a button code
convert_btn = Button(window, text='convert', bg='purple', fg='white', width=14, command=convert)
convert_btn.grid(row=3, column=0, padx=15, pady=10)

clear_btn = Button(window, text='clear', bg='red', fg='white', width=14, command=clea)
clear_btn.grid(row=3, column=1, padx=1, pady=15)

window.mainloop()
