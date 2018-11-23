import tkinter as tk
from tkinter import ttk
from components.ClaseBiologia import ClaseBiologia
from components.ListBox import ListBox
from components.Detalles import Detalles
from helpers.colors import grisOscuro
from models.Animal import Animal

perro = Animal(descripcion='Este es perro', urlImage='./perro_1.png')


class Ventana(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(bg = grisOscuro)
        self.pack()

        """ MODIFICAR ESTE ARRAY SIMPLE CON UNA ARRAY DE OBJETOS ANIMALES """
        self.listBox = ListBox(self)
        self.caninos = ClaseBiologia(
            root = self,
            file = 'mastin.png',
            text = 'Caninos',
            x = 100,
            y = 120,
            data = [perro,perro,perro]
        )
        
        self.aracnidos = ClaseBiologia(
            root = self,
            file = 'arana.png',
            text = 'Aracnidos',
            x = 580,
            y = 120,
            data = [perro,perro,perro]
        )

        self.aves = ClaseBiologia(
            root = self,
            file = 'loros.png',
            text = 'Aves',
            x = 100,
            y = 330,
            data = [perro,perro,perro]
        )
        
        self.pez = ClaseBiologia(
            root = self,
            file = 'pez.png',
            text = 'Peces',
            x = 580,
            y = 330,
            data = [perro,perro,perro]
        )

        self.detalles = Detalles(root = self)

    def handleClickImage(self,e,data):
        self.listBox.delete(0,tk.END)
        self.listBox.data = data
        for element in data:
            self.listBox.insert(tk.END,element.descripcion)
    
    def handleListBoxSelect(self,e,data):
        index = self.listBox.curselection()[0]
        """ AQUI DEBE SER MODIFICADO PARA FUNCIONAR BN CON OBJETOS ANIMALES """
        self.detalles.setDescription(objeto= data[index])
        self.detalles.place(x = 280, y = 160)

    def handleBackDetalles(self,e):
        self.detalles.place_forget()

root = tk.Tk()
root.title("BC Proyecto de Ciro de Mrd")

windows = ttk.Notebook(root)
windows.pack(fill = 'both', expand = 'yes')
pestaña1 = Ventana(root = root)
pestaña2 = Ventana(root = root)

windows.add(pestaña1, text = "Pestaña 1")
windows.add(pestaña2, text = "Pestaña 2")

root.mainloop()
