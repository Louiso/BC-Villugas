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
        
        self.s = tk.Scrollbar(self.body)
        self.descripcion = tk.Text(self.body,height=21.5, width=75)
                
        self.descripcion.pack(side=tk.LEFT, fill=tk.Y)
        self.s.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.s.config(command=self.descripcion.yview)
        #self.descripcion.config(width = 70, height = 18, yscrollcommand=self.s.set)
        self.descripcion.config(yscrollcommand=self.s.set)

        self.descripcion.insert(tk.INSERT,objeto.fasta)
        

    def setDescription(self,objeto = Animal()):
        #self.descripcion.delete('1.0',tk.END)
        self.descripcion.insert(tk.INSERT, "\n\n"+ objeto.fasta)

    def nom(self,objeto = Animal()):
        self.label = tk.Label(self, text = objeto.proteina)
        self.label.config(anchor = tk.CENTER, pady= 5, bg = 'gray', width = 77)
        self.label.place(x=0,y=0)

