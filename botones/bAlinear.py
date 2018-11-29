
import tkinter as tk
from components.arbolG import Arbol
import math

class bAlinear(tk.Button):
    def __init__(self, root = None, file = None,  text = '', x = 0 , y  = 0, proteina = ""):
        super().__init__(root, text = text)
        self.proteina = proteina
        self.root = root
        self.config(compound = tk.RIGHT, width = 9, height = 3)
        self.place(x  = x , y = y)

        self.bind('<Button-1>', lambda e: root.generaAln())    