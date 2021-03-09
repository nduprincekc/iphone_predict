import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame

musicplayer = tk.Tk()
musicplayer.title('kc emma')
musicplayer.geometry('420x320')


directory = askdirectory()
os.chdir(directory)
songlist =os.listdir()
playlist =tk.Listbox(musicplayer,font ='Helvetica 12 bold', bg = 'yellow', selectmode = tk.SINGLE)

for item in songlist:
    po=0
    playlist.insert(po, item)
    pos = po + 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


button1 = tk.Button(musicplayer, width=4, height=3, text='PLAY', command=play, bg='red', fg='white')
button2 = tk.Button(musicplayer, width=4, height=3, text='STOP', command=stop, bg='red', fg='white')
button3 = tk.Button(musicplayer, width=4, height=3, text='PAUSE', command=pause, bg='red', fg='white')
button4 = tk.Button(musicplayer, width=4, height=3, text='UNPAUSE', command=unpause, bg='red', fg='white')

var = tk.StringVar
song_man = tk.Label(musicplayer, font='Helvetica 12 bold', textvariable=var)
song_man.pack()
button1.pack(fill='x')
button2.pack(fill='x')
button3.pack(fill='x')
button4.pack(fill='x')

playlist.pack(fill='both',expand='yes')


musicplayer.mainloop()
