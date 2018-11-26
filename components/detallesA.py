import tkinter as tk
from models.Animal import Animal
from helpers.helpers import resize
from helpers.colors import grisOscuro

class detallesA(tk.Frame):
    def __init__(self, root = None, objeto = Animal()):
        super().__init__(root)
        
#################################################################################################
        self.body = tk.Frame(self)
        self.body.config(width = 510, height = 242)
        self.body.pack( side = tk.BOTTOM )

        self.descripcion = tk.Text(self.body)
        self.descripcion.config(width = 70, height = 18)
        self.descripcion.insert(tk.INSERT,objeto.descripcion)
        self.descripcion.place(x = 5, y = 35)

    def setDescription(self,objeto = Animal()):
        self.descripcion.delete('1.0',tk.END)
        self.descripcion.insert(tk.INSERT,objeto.descripcion)

    def nom(self,objeto = Animal()):
        self.label = tk.Label(self, text = objeto.proteina)
        self.label.config(anchor = tk.CENTER, pady= 10, bg = 'gray', width = 73)
        self.label.place(x=0,y=0)

