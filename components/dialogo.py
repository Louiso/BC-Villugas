import tkinter as tk

from models.Animal import Animal
from helpers.helpers import resize
from helpers.colors import grisOscuro,grisClaro
class dialogo(tk.Frame):
    def __init__(self, root = None, objeto = Animal()):
        super().__init__(root)

        #self.label = tk.Label(self, text = 'Ayuda')
        #self.label.config(anchor = tk.CENTER, pady= 10, bg = 'gray', width = 55)
        #self.label.pack(side = tk.TOP)
#################################################################################################
        self.body = tk.Frame(self)
        self.body.config(width = 648, height = 430)
        self.body.pack( side = tk.BOTTOM )
        
        """ FOTO DEL ANIMAL """
        self.photo = tk.PhotoImage(file = objeto.urlImage)
        self.photo = resize( self.photo, 120 , 120 )

        self.labelPhoto = tk.Label(self.body, image = self.photo, bg = grisOscuro)
        self.labelPhoto.place(x = 0 , y = 0)

        self.descripcion = tk.Text(self.body)
        self.descripcion.config(width = 210, height = 31)
        self.descripcion.insert(tk.INSERT,objeto.descripcion)
        self.descripcion.place(x = 0, y = 150)
#################################################################################################
        self.button = tk.Button(self.body, text = 'Ok')
        self.button.place(x = 100, y = 280)
        self.button.bind('<Button-1>', lambda e: root.handleBackDetalles2(e))

    def setDescription(self,objeto = Animal()):
        print(objeto.urlImage)
        self.photo = tk.PhotoImage(file = objeto.urlImage)
        self.photo = resize( self.photo, 120 , 120 )
        self.labelPhoto.config(image = self.photo)
        self.labelPhoto.place(x = 65, y = 10 )
        self.descripcion.delete('1.0',tk.END)
        self.descripcion.insert(tk.INSERT,objeto.descripcion)