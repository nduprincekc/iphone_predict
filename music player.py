import pygame
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import os,tkinter


m = Tk()
m.title('kc emma music player')
var = tk.StringVar

# creating the music dimension
m.geometry('400x500')

dice = askdirectory()


os.chdir(dice)

song_list = os.listdir()

# creating a playlist
playlist = tk.Listbox(m, font='Cambria 14', bg ='cyan2', selectmode= tk.SINGLE)


for item in song_list:
    pos = 0
    playlist.insert(pos,item)

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()


def stop():
    #pygame.mixer.music.stop()
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()

def unpause():
    pygame.mixer.music.unpause()


def pause():
    pygame.mixer.music.pause()


But_play = tk.Button(m, height=3, width = 5, text='Play Music', font='Cambria 14 bold', command =play, bg='green',fg='black')
But_stop = tk.Button(m, height=3, width = 5, text='Stop Music', font='Cambria 14 bold', command =stop(), bg='green',fg='black')
But_pause = tk.Button(m, height=3, width = 5, text='Pause Music', font='Cambria 14 bold', command =pause, bg='green',fg='black')
But_resume = tk.Button(m, height=3, width = 5, text='resume Music', font='Cambria 14 bold', command =unpause, bg='green',fg='black')

But_play.pack(fill='x')
But_resume.pack(fill='x')
But_pause.pack(fill='x')
But_stop.pack(fill='x')


playlist.pack(fill='x', expand='yes')
var = tk.StringVar()


song_title= tk.Label(m,font='Cambria 12 bold', textvariable = var)
m.mainloop()
