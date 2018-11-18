import tkinter as tk
from components.ClaseBiologia import ClaseBiologia

class Ventana(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(bg = 'gray10')
        self.pack()

        caninos = ClaseBiologia(
            root = self,
            file = 'mastin.png',
            text = 'Caninos',
            x = 100,
            y = 120
        )
        
        aracnidos = ClaseBiologia(
            root = self,
            file = 'arana.png',
            text = 'Aracnidos',
            x = 580,
            y = 120
        )

        aves = ClaseBiologia(
            root = self,
            file = 'loros.png',
            text = 'Aves',
            x = 100,
            y = 330
        )
        
        pez = ClaseBiologia(
            root = self,
            file = 'pez.png',
            text = 'Peces',
            x = 580,
            y = 330
        )



root = tk.Tk()
root.title("BC Proyecto de Ciro de Mrd")


app = Ventana(root = root)
app.mainloop()
