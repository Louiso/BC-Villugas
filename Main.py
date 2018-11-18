import tkinter as tk
from components.ClaseBiologia import ClaseBiologia
from components.ListBox import ListBox
from components.Detalles import Detalles
from helpers.colors import grisOscuro

class Ventana(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(bg = grisOscuro)
        self.pack()


        self.listBox = ListBox(self)
        self.caninos = ClaseBiologia(
            root = self,
            file = 'mastin.png',
            text = 'Caninos',
            x = 100,
            y = 120,
            data = ['perro','lobo','can']
        )
        
        self.aracnidos = ClaseBiologia(
            root = self,
            file = 'arana.png',
            text = 'Aracnidos',
            x = 580,
            y = 120,
            data = ['arana','viuda negra','charlotte']
        )

        self.aves = ClaseBiologia(
            root = self,
            file = 'loros.png',
            text = 'Aves',
            x = 100,
            y = 330,
            data = ['tucan','gallito de las rocas','ella no te ama >:v']
        )
        
        self.pez = ClaseBiologia(
            root = self,
            file = 'pez.png',
            text = 'Peces',
            x = 580,
            y = 330,
            data = ['pez globo','trucha','campeon del ACM :)']
        )

        self.detalles = Detalles(root = self)

    def handleClickImage(self,e,data):
        self.listBox.delete(0,tk.END)
        for element in data:
            self.listBox.insert(tk.END,element)
    
    def handleListBoxSelect(self,e):
        index = self.listBox.curselection()[0]
        self.detalles.setDescription(text = "Sera")
        self.detalles.place(x = 280, y = 160)

    def handleBackDetalles(self,e):
        self.detalles.place_forget()


        


root = tk.Tk()
root.title("BC Proyecto de Ciro de Mrd")


app = Ventana(root = root)
app.mainloop()
