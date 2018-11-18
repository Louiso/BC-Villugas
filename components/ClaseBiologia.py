import tkinter as tk
import math
from helpers.helpers import resize
class ClaseBiologia(tk.Frame):
    def __init__(self, root = None, file = '', text = '', x = 0, y = 0):
        super().__init__(root)
        
        width = 120
        height = 120
        
        self.photo = tk.PhotoImage(file = file)
        self.photo = resize( self.photo, width , height )

        img = tk.Label(self, image = self.photo, bg = 'gray25')

        label = tk.Label(self, text = text)
        label.config(anchor = tk.CENTER, pady= 10, bg = 'gray75', width = 16)
        img.pack( side = tk.TOP)
        label.pack( side = tk.BOTTOM )
        self.place(x = x , y = y)