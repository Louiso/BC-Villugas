import tkinter as tk
import math
from helpers.helpers import resize
from components.ListBox import ListBox
from helpers.colors import grisMedio, grisClaro

class ClaseAnalisis(tk.Frame):
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
        width = 80
        height = 80
        
        self.photo = tk.PhotoImage(file = file)
        self.photo = resize( self.photo, width , height )

        self.img = tk.Label(self, image = self.photo, bg = grisMedio)

        self.label = tk.Label(self, text = text)
        self.label.config(anchor = tk.CENTER, pady= 10, bg = grisClaro, width = 10)
        self.img.pack( side = tk.TOP)
        self.label.pack( side = tk.BOTTOM )
        self.place(x = x , y = y)
                

        self.img.bind('<Button-1>', lambda e: root.handleClickImage(e,self.data))
        self.label.bind('<Button-1>', lambda e: root.handleClickImage(e,self.data))
        