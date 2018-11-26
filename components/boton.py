
import tkinter as tk
import math

class Boton(tk.Button):
    def __init__(self, root = None, file = None , width = 100, height = 100,  text = '', x = 0 , y  = 0):
        super().__init__(root, text = text)
        self.root = root
        self.config(compound = tk.RIGHT, width = 9, height = 3)
        self.place(x  = x , y = y)