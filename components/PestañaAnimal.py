import tkinter as tk
from components.ListBox import ListBox
from components.Detalles import Detalles
from helpers.colors import grisOscuro
from models.Animal import Animal
from components.ClaseBiologia import ClaseBiologia


perro = Animal(descripcion='Este es perro', urlImage='./img/perro_1.png')

vaca = "Es una especie de marsopa (delfines pequenos), es una especie endemica que actualmente se encuentra en peligro de extincion su habitat es el golfo de California y la peninsula baja de California."
delfinBot = "El delfin mular o de nariz de botella, de la familia Delphinidae. De las mas de 30 especies de delfines que existen, es la mas comun y mas conocida de la familia."
orca = "La orca es una especie de cetaceo odontoceto perteneciente a la familia Delphinidae, que habita en todos los oceanos del planeta. Es la especie mas grande de delfinido y la unica existente actual reconocida dentro del genero Orcinus. Este cetaceo posee una complexion robusta e hidrodinamica"
BallenasMinke = "Rorcuales Minke o ballenas Minke es el nombre por el que son conocidos en la actualidad dos especies de misticetos balenopteridos: Hacia el ano 1780, estos rorcuales eran identificados como una sola especie: Balaena rostrata"
Cachalote = "El cachalote es una especie de mamifero marino del orden Cetacea del suborden Odontoceti. El cachalote es el unico miembro del genero Physeter y es una de las tres especies vivientes de la familia Physeteridae, junto al cachalote pigmeo y cachalote enano"

petirrojo="Uno de los mas populares y facilmente reconocibles, al que se distingue por su llamativa mancha anaranjada en el pecho , la garganta y la cara , en invierno resulta muy en casi cualquier ambiente ,incluyendo parques y jardines,pero en primavera cría preferentemente en parques frescos,es territorial tanto en invierno como en verano, y muy a menudo suele dejarse ver entre los arbusto o en el suelo mientras busca insectos."
gorrion="El familiar y animado gorrion que se ve alrededor de asentamientos 	humanos de todos los tamanos. Los machos tienen capuchon y 	mejillas de color gris y una mancha de color marron rojizo detras 	de cada ojo. "
paloma="Es una especie de ave columbiforme de la familia Columbidae nativa del sur de Eurasia y el norte de Africa. Es el ancestro de las palomas domesticas, con las que se cruza, lo que demuestra su estrecho parentesco. Anida en las paredes rocosas. Se parece mucho a la paloma domestica gris tipica, pero las domesticas presentan gran variedad de coloraciones y formas diferentes"
gallo="Es una especie tropical de la familia Phasianidae nativa del sudeste asiatico. Se considera el ancestro de los gallos y gallinas domesticos, con algo de hibridación del gallo gris. El gallo silvestre fue domesticado al menos hace siete mil años en Asia, y posteriormente llevado a todo el mundo. La variedad domestica se cria globalmente como fuente de carne y huevos."
ave="Esta pequena ave presenta una longitud de 14 cm, una envergadura de 22 cm y un peso de unos 16 o 20 g. El diámetro del iris, de color castaño, ronda los 3,5 mm.En cuanto al plumaje, se describe de un color apagado y en conjunto nada vistoso. Tanto macho como hembra presentan tonos pardos grisáceos en las partes superiores, y mas blancuzcos en las inferiores. Pecho y flancos de un color levemente amarillento."

Garrapata = "Los ixodoideos (Ixodoidea) son una superfamilia de acaros, conocidos vulgarmente como garrapatas. Son ectoparasitos hematofagos (se alimentan de sangre) y son vectores de numerosas enfermedades infecciosas entre las que destacan el tifus o la enfermedad de Lyme. Son los acaros de mayor tamano."
Escorpion = "Los escorpiones son de un orden de apendices en forma de pinzas y una cola acabada en un aguijon provisto de veneno .Habitan preferentemente en terrenos arenosos o rocosos o en las superficies tropicales y  deserticas."
Arana = "Por regla general son animales solitarios y depredadores de pequeños insectos a los cuales pueden dar caza a traves de tecnicas muy variadas. Algunas, de hecho, poseen potentes venenos los cuales un pequena cantidad, puede acabar con la vida de un ser humano."
alacran = "Es frecuente encontrarlo en el campo y su picadura no es potente y a veces el aguijon ni siquiera traspasa la piel.Esta especie comprende a un aracnido de mediano a gran tamano, los adultos llegan a medir unos 60 mm de largo."
Tarantula = "La tarantula cebra de Costa Rica o tarantula de rodillas rayadas (Aphonopelma seemanni), habita en la mayor parte del oeste de Costa Rica, asi como en otras partes de America Central, como Guatemala, Honduras y Nicaragua. "

data = [
    Animal(
        name='Vaquita Marina',
        descripcion=vaca,
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
        descripcion=vaca,
        urlImage='./img/petirrojo1.png'),
    Animal(
        name='Gorrión común (Passer domesticus)',
        descripcion=gorrion,
        urlImage='./img/gorrion1.png'
    ),
     Animal(
        name='Paloma Bravía (Columba livia)',
        descripcion=paloma,
        urlImage='./img/paloma1.png'),
      Animal(
        name='Gallo Bankiva (Gallus gallus)',
        descripcion=gallo,
        urlImage='./img/gallo1.png'),
      Animal(
        name='Curruca Mosquitera  (Sylvia borin)',
        descripcion=ave,
        urlImage='./img/sylvia1.png'),      
        
]

Cetaceos = [
    Animal(
        name="Vaquita Marina",
        descripcion=vaca,
        urlImage='./img/vacaMarina.png'),
    Animal(
        name='Delfin Nariz de Botella',
        descripcion=delfinBot,
        urlImage='./img/botella.png'
    ),
     Animal(
        name='Orca',
        descripcion=orca,
        urlImage='./img/orca.png'),
      Animal(
        name='Ballena Minke',
        descripcion=BallenasMinke,
        urlImage='./img/minke.png'),
      Animal(
        name='Cachalote',
        descripcion=Cachalote,
        urlImage='./img/cachalote.png'),              
]

insectos = [
    Animal(
        name="Garrapata",
        descripcion=Garrapata,
        urlImage='./img/garrapata.png'),
    Animal(
        name='Escorpion',
        descripcion=Escorpion,
        urlImage='./img/escorpion.png'
    ),
     Animal(
        name='Arana',
        descripcion=Arana,
        urlImage='./img/arana2.png'),
      Animal(
        name='Alacran',
        descripcion=alacran,
        urlImage='./img/alacran.png'),
      Animal(
        name='Tarantula Cebra de Costa',
        descripcion=Tarantula,
        urlImage='./img/tarantula.png'),              
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
            file = './img/mastin.png',
            text = 'Caninos',
            x = 100,
            y = 120,
            data = data
        )
        
        self.aracnidos = ClaseBiologia(
            root = self,
            file = './img/arana.png',
            text = 'Aracnidos',
            x = 580,
            y = 120,
            data = insectos
        )

        self.aves = ClaseBiologia(
            root = self,
            file = './img/loros.png',
            text = 'Aves',
            x = 100,
            y = 330,
            data = data2
        )
        
        self.pez = ClaseBiologia(
            root = self,
            file = './img/pez.png',
            text = 'Cetaceos',
            x = 580,
            y = 330,
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