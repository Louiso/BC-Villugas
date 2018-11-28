import tkinter as tk
import math
""" Zoom: agranda n veces la imagen
    subsample : corta n veces la imagen en los ejes X, Y
"""
class Button(tk.Button):
    def __init__(self, root = None, file = None , width = 100, height = 100,  text = '', x = 0 , y  = 0):
        super().__init__(root, text = text)
        self.root = root
        self.image = tk.PhotoImage(file=file)
        scaleX = math.floor(self.image.width() / width) 
        scaleY = math.floor(self.image.height() / height)
        """ subsample divide n veces la imagen """
        self.image = self.image.subsample(x = scaleX, y = scaleY)
        self.config(image = self.image , compound = tk.RIGHT, width = 100, height = 100)
        self.place(x  = x , y = y)