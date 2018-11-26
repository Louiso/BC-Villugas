import tkinter as tk
from components.ListBox import ListBox
from components.Detalles import Detalles
from helpers.colors import grisOscuro
from models.Animal import Animal
from components.ClaseAnalisis import ClaseAnalisis

data = [
    Animal(
        name='Vaquita Marina',
        descripcion="vaca",
        urlImage='./img/vaca.png'),
    Animal(
        name='Perro',
        descripcion='Texto de descripcion del animal Perro',
        urlImage='./img/mastin.png'
    ),
]
data2 = [
    Animal(
        name='Petirrojo europeo (Erithacus rubecula)',
        descripcion="vaca",
        urlImage='./img/petirrojo1.png'),
    Animal(
        name='Gorrión común (Passer domesticus)',
        descripcion="gorrion",
        urlImage='./img/gorrion1.png'
    ),
     Animal(
        name='Paloma Bravía (Columba livia)',
        descripcion="paloma",
        urlImage='./img/paloma1.png'),
      Animal(
        name='Gallo Bankiva (Gallus gallus)',
        descripcion="gallo",
        urlImage='./img/gallo1.png'),
      Animal(
        name='Curruca Mosquitera  (Sylvia borin)',
        descripcion="ave",
        urlImage='./img/sylvia1.png'),      
        
]

Cetaceos = [
    Animal(
        name="Vaquita Marina",
        descripcion="vaca",
        urlImage='./img/vacaMarina.png'),
    Animal(
        name='Delfin Nariz de Botella',
        descripcion="delfinBot",
        urlImage='./img/botella.png'
    ),
     Animal(
        name='Orca',
        descripcion="orca",
        urlImage='./img/orca.png'),
      Animal(
        name='Ballena Minke',
        descripcion="BallenasMinke",
        urlImage='./img/minke.png'),
      Animal(
        name='Cachalote',
        descripcion="Cachalote",
        urlImage='./img/cachalote.png'),              
]

insectos = [
    Animal(
        name="Garrapata",
        descripcion="Garrapata",
        urlImage='./img/garrapata.png'),
    Animal(
        name='Escorpion',
        descripcion="Escorpion",
        urlImage='./img/escorpion.png'
    ),
     Animal(
        name='Arana',
        descripcion="Arana",
        urlImage='./img/arana2.png'),
      Animal(
        name='Alacran',
        descripcion="alacran",
        urlImage='./img/alacran.png'),
      Animal(
        name='Tarantula Cebra de Costa',
        descripcion="Tarantula",
        urlImage='./img/tarantula.png'),              
]

class PestañaAnalisis(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(bg = grisOscuro)
        self.pack()

        self.title = tk.Label(self, text = 'CIRO DE MRD >:v')
        self.title.config(anchor = tk.CENTER, pady= 20, bg = grisOscuro, font= 1, fg = 'white', width = 80)
        self.title.place(x = 0 , y = 0)

        """ MODIFICAR ESTE ARRAY SIMPLE CON UNA ARRAY DE OBJETOS ANIMALES """
        self.listBox = ListBox(self,w = 30, h = 20 ,px=43,py=250)
        #self.fasta = 
        self.caninos = ClaseAnalisis(
            root = self,
            file = './img/mastin.png',
            text = 'Caninos',
            x = 55,
            y = 80,
            data = data
        )
        
        self.aracnidos = ClaseAnalisis(
            root = self,
            file = './img/arana.png',
            text = 'Aracnidos',
            x = 255,
            y = 80,
            data = insectos
        )

        self.aves = ClaseAnalisis(
            root = self,
            file = './img/loros.png',
            text = 'Aves',
            x = 455,
            y = 80,
            data = data2
        )
        
        self.pez = ClaseAnalisis(
            root = self,
            file = './img/pez.png',
            text = 'Cetaceos',
            x = 655,
            y = 80,
            data = Cetaceos
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
        self.detalles.place(x = 242, y = 120)

    def handleBackDetalles(self,e):
        self.detalles.place_forget()