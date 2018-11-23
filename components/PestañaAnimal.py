import tkinter as tk
from components.ListBox import ListBox
from components.Detalles import Detalles
from helpers.colors import grisOscuro
from models.Animal import Animal
from components.ClaseBiologia import ClaseBiologia


perro = Animal(descripcion='Este es perro', urlImage='./perro_1.png')
vaca = "Es una especie de marsopa (delfines pequenos), es una especie endemica que actualmente se encuentra en peligro de extincion su habitat es el golfo de California y la peninsula baja de California."

data = [
    Animal(
        name='Vaquita Marina',
        descripcion=vaca,
        urlImage='./vaca.png'),
    Animal(
        name='Perro',
        descripcion='Texto de descripcion del animal Perro',
        urlImage='./mastin.png'
    ),
]

class PestañaAnimal(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(bg = grisOscuro)
        self.pack()

        self.title = tk.Label(self, text = 'CIRO DE MRD >:v')
        self.title.config(anchor = tk.CENTER, pady= 20, bg = grisOscuro, font= 1, fg = 'white', width = 80)
        self.title.place(x = 0 , y = 0)

        """ MODIFICAR ESTE ARRAY SIMPLE CON UNA ARRAY DE OBJETOS ANIMALES """
        self.listBox = ListBox(self)
        self.caninos = ClaseBiologia(
            root = self,
            file = 'mastin.png',
            text = 'Caninos',
            x = 100,
            y = 120,
            data = data
        )
        
        self.aracnidos = ClaseBiologia(
            root = self,
            file = 'arana.png',
            text = 'Aracnidos',
            x = 580,
            y = 120,
            data = data
        )

        self.aves = ClaseBiologia(
            root = self,
            file = 'loros.png',
            text = 'Aves',
            x = 100,
            y = 330,
            data = data
        )
        
        self.pez = ClaseBiologia(
            root = self,
            file = 'pez.png',
            text = 'Peces',
            x = 580,
            y = 330,
            data = data
        )

        self.detalles = Detalles(root = self)

    def handleClickImage(self,e,data):
        self.listBox.delete(0,tk.END)
        self.listBox.data = data
        for element in data:
            self.listBox.insert(tk.END,element.name)
    
    def handleListBoxSelect(self,e,data):
        index = self.listBox.curselection()[0]
        """ AQUI DEBE SER MODIFICADO PARA FUNCIONAR BN CON OBJETOS ANIMALES """
        self.detalles.setDescription(objeto= data[index])
        self.detalles.place(x = 280, y = 160)

    def handleBackDetalles(self,e):
        self.detalles.place_forget()