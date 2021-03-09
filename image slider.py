from itertools import cycle
import tkinter as tk

class App(tk.Tk):
    def __init__(self,image_files,x,y,delay):
        tk.Tk.__init__(self)
        self.geometry('400x400')
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(files=image),image)
                               for image in image_files )
        self.pictures_display =tk.Label(self)
        self.pictures_display.pack()

    def show_slides(self):
        #cycle through the images

        img_object,img_name =next(self.pictures)
        self.pictures_display.config(image=img_object)

        self.title(img_name)
        self.after(self.delay,self.show_slides())
    def run(self):
        self.mainloop()


delay =3500

image_files = [
    'ic.png',
    'back.png',
    'kc.jpg'
    'kc.jpg'
    'kc.jpg'
    'kc.jpg'

]

app = App(image_files,delay)
app.show_slides()
app.run()
