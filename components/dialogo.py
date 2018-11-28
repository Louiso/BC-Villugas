import tkinter as tk

from models.Animal import Animal
from helpers.helpers import resize
from helpers.colors import grisOscuro,grisClaro
class dialogo(tk.Frame):
    def __init__(self, root = None, imagen = "",gift =""):
        super().__init__(root)
        self.imagen = imagen
        self.gift = gift
        self.body = tk.Frame(self)
        self.body.config(width = 648, height = 430)
        self.body.pack( side = tk.BOTTOM )
        
        """ FOTO DEL ANIMAL """
        self.photo = tk.PhotoImage(file = imagen)
        self.photo = resize( self.photo, 600 , 400 )

        self.labelPhoto = tk.Label(self.body, image = self.photo, bg = grisClaro)
        self.labelPhoto.place(x = 30 , y = 15)

#################################################################################################
        self.button = tk.Button(self.body, text = 'Ok')
        self.button.place(x = 300, y = 380)
        self.button.bind('<Button-1>', lambda e: root.handleBackDetalles2(e))

    def setDescription(self,objeto = Animal()):
        print(objeto.urlImage)
        self.photo = tk.PhotoImage(file = objeto.urlImage)
        self.photo = resize( self.photo, 120 , 120 )
        self.labelPhoto.config(image = self.photo)
        self.labelPhoto.place(x = 65, y = 10 )