import tkinter
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title = 'kc emma'
root.geometry('200x100')
root.iconbitmap('C:/Users/us er/PycharmProjects/iwe/ic.png')

# init

pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title='choose a song ', filetypes=(('mp3 files', 'mp3'),))
    song = song.replace('C:/Users/us er', '')
    song = song.replace('.mp3', '')

    song_box.insert(END, song)


#    print(song)


# play button

def play1():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/user/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


song_box = Listbox(root, bg='black', fg='green', width=20, height=2)

song_box.pack(pady=10)

# creating button

back_btn = PhotoImage(file='stop.png')
pause = PhotoImage(file='stop.png')
stop = PhotoImage(file='stop.png')
kcv = PhotoImage(file='stop.png')
play = PhotoImage(file='stop.png')
# create frame

control_frame = Frame(root)
control_frame.pack()
## create player contorl button

back_btn1 = Button(control_frame, image=back_btn, borderwidth=0)
pause2 = Button(control_frame, image=pause, borderwidth=0)
stop3 = Button(control_frame, image=stop, borderwidth=0)
kcv4 = Button(control_frame, image=kcv, borderwidth=0)
play5 = Button(control_frame, image=play, borderwidth=0, command='play')

back_btn1.grid(row=0, column=1, padx=5)
pause2.grid(row=0, column=2, padx=5)
stop3.grid(row=0, column=3, padx=5)
kcv4.grid(row=0, column=4, padx=5)
play5.grid(row=0, column=5, padx=5)

mymenu = Menu(root)
root.config(menu=mymenu)

# song_menu

add_song_menu = Menu(mymenu)
mymenu.add_cascade(label='Add songs', menu=add_song_menu)
add_song_menu.add_command(label='add one song to the playlist', command=add_song)

root.mainloop()
