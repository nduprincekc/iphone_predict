import tkinter as tk
from tkinter import Tk,Label,Button,Entry,Message
import pygeoip

# user = input('Enter the 1p address: ')


root = Tk()
root.title('kc emma')
root.geometry('320x220')
root.resizable(width=False, height=False)
root.config(background='green')


'''the main geolocation code'''


def geo():
    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    res = gip.record_by_addr(user)
    for key,val in res.items():
        print('%s : %s' % (key,val))

def box():
    passK


but1 = Button(root, text='check')
but1.grid(row=97,column=7)

lbl = Label(root, text='enter the ip adress: ', fg='blue')
lbl.grid(row=1,column=2)
ent1 = Entry(root,)
ent1.grid(row=1,column=3)

# root.pack()

root.mainloop()
