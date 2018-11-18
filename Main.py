import tkinter as tk
from components.Button import Button
class Ventana(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(cursor = 'spider', bg = 'green')
        self.pack()
        boton = Button( root = self, text='Spider', file = "arana.png", width = 100, height = 100)
        boton.place(x = 20, y = 20)


root = tk.Tk()
root.title("BC Proyecto de Ciro de Mrd")


app = Ventana(root = root)
app.mainloop()
