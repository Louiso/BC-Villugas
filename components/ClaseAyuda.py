import tkinter as tk
import math
from helpers.helpers import resize
from components.ListBox import ListBox
from helpers.colors import grisMedio, grisClaro, grisOscuro

class ClaseAyuda(tk.Frame):
    def __init__(   self, 
                    root = None,
                    file = '',
                    text = '',
                    x = 0,
                    y = 0,
                    data = []
                ):
        super().__init__(root)
        
        self.data = data
        width = 50
        height = 50
        
        self.photo = tk.PhotoImage(file = file)
        self.photo = resize( self.photo, width , height )

        self.img = tk.Label(self, image = self.photo, bg = grisOscuro)
        self.img.pack( side = tk.TOP)
        self.place(x = x , y = y)
                

        self.img.bind('<Button-1>', lambda e: root.handleClickImage2(e,self.data))
        