import tkinter as tk
from components.ListBox import ListBox
from components.Detallesp import Detalles
from helpers.colors import grisOscuro
from models.Animal import Animal
from components.ClaseBiologia import ClaseBiologia
from models.Proteina import  Proteina

cry4 = "Dos investigaciones han concluido que esta proteína le permite a las aves ver el campo magnético terrestre y orientarse en vuelo .esta proteína está situada en la zona de la retina que recibe más luz y sus niveles aumenta en la estación migratoria."
tmie = "Este gen codifica una proteina transmembrana del oido interno. Los estudios en ratones sugieren que este gen es necesario para la maduracion posnatal normal de las celulas ciliadas sensoriales en la coclea, incluido el desarrollo correcto de los paquetes de estereocilios. "
rodopsina = "La rodopsina es una proteina transmembranal que, en humanos, se encuentra en los discos de los bastones de la retina. Consta de una parte proteica, opsina, y una no proteica que es un derivado de la vitamina A que es el 11-cis-retinal. Es inestable y se altera facilmente con la energia luminica, se decolora y descompone por exposicion a la luz y se regenera con la oscuridad."
cithocrome = "La citocromo c oxidasa I es la subunidad principal del complejo citocromo c oxidasa . Las mutaciones en MT-CO1 se han asociado con neuropatia optica hereditaria de Leber (LHON), anemia sideroblastica idiopatica adquirida, deficiencia de Complejo IV , cancer colorrectal , sordera neurosensorial y mioglobinuria recurrente."

data = [
    Proteina(
        name='Cry4',
        descripcion=cry4
        )
    
]

data2 = [
    Proteina(
        name='Tmie',
        descripcion=tmie
        )    
]

data3 = [
    Proteina(
        name='rodopsina',
        descripcion=rodopsina
        )    
]

data4 = [
    Proteina(
        name='Cithocrome',
        descripcion=cithocrome
        )    
]




class PestañaProteinas(tk.Frame):
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
            file = 'cry41.png',
            text = 'CRY4',
            x = 100,
            y = 120,
            data = data
        )
        
        self.aracnidos = ClaseBiologia(
            root = self,
            file = 'rodopsina.png',
            text = 'Rodopsina',
            x = 580,
            y = 120,
            data = data3
        )

        self.aves = ClaseBiologia(
            root = self,
            file = 'nariz1.png',
            text = 'Cytochrome',
            x = 100,
            y = 330,
            data = data4
        )
        
        self.pez = ClaseBiologia(
            root = self,
            file = 'oido1.png',
            text = 'Tmie',
            x = 580,
            y = 330,
            data = data2
        )

        self.detalles = Detalles(root = self)

    def handleClickImage(self,e,data):
        #self.listBox.delete(0,tk.END)
        #self.listBox.data = data
        #for element in data:
         #   self.listBox.insert(tk.END,element.name)
        #index = self.listBox.curselection()[0]
        """ AQUI DEBE SER MODIFICADO PARA FUNCIONAR BN CON OBJETOS ANIMALES """
        self.detalles.setDescription(objeto= data[0])
        self.detalles.place(x = 242, y = 120)

    
   # def handleListBoxSelect(self,e,data):
    #    index = self.listBox.curselection()[0]
     #   """ AQUI DEBE SER MODIFICADO PARA FUNCIONAR BN CON OBJETOS ANIMALES """
      #  self.detalles.setDescription(objeto= data[index])
       # self.detalles.place(x = 280, y = 160)

    def handleBackDetalles(self,e):
        self.detalles.place_forget()