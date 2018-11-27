import tkinter as tk
from components.ListBox import ListBox
from components.detallesA import detallesA
from components.boton import Boton
from helpers.colors import grisOscuro
from models.Animal import Animal
from components.ClaseAnalisis import ClaseAnalisis
from components.arbolG import Arbol

data = [
    Animal(
        name='Perro',
        descripcion="vaca",
        urlImage='./img/vaca.png',
        proteina = "Rodopsina",
        fasta=">NP_001008277.1 rhodopsin [Canis lupus familiaris] MNGTEGPNFYVPFSNKTGVVRSPFEYPQYYLAEPWQFSMLAAYMFLLIVLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNVEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLAGWSSLLSHSPLVLRYIPEGMQCSCGIDYYTLKPEINNESFVIYMFVVHFAIPMIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSDFGPIFMTLPAFFAKSSSIYNPVIYIMMNKQFRNCMITTLCCGKNPLGDDEASASASKTETSQVAPA"),
    Animal(
        name='Zorro Artico',
        descripcion='Texto de descripcion del animal Perro',
        urlImage='./img/mastin.png',
        proteina = "Rodopsina",
        fasta=">ABB21977.1 rhodopsin, partial [Vulpes lagopus] VIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVA"
    ),
    Animal(
        name='Lobo',
        descripcion="vaca",
        urlImage='./img/vaca.png',
        proteina = "Rodopsina",
        fasta=">ABB21976.1 rhodopsin, partial [Canis lupus] VIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVA"),
    Animal(
        name='Zorro Comun',
        descripcion='Texto de descripcion del animal Perro',
        urlImage='./img/mastin.png',
        proteina = "Rodopsina",
        fasta=">XP_025872700.1 rhodopsin [Vulpes vulpes] MNGTEGPNFYVPFSNKTGVVRSPFEYPQYYLAEPWQFSMLAAYMFLLIVLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNVEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLAGWSRYIPEGMQCSCGIDYYTLKPEINNESFVIYMFVVHFAIPMFVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSDFGPIFMTLPAFFAKSSSIYNPVIYIMMNKQFRNCMITTLCCGKNPLGDDEASASASKTETSQVAPA"
    ),Animal(
        name='Dingo',
        descripcion="vaca",
        urlImage='./img/vaca.png',
        proteina = "Rodopsina",
        fasta=">XP_025305095.1 rhodopsin [Canis lupus dingo] MNGTEGPNFYVPFSNKTGVVRSPFEYPQYYLAEPWQFSMLAAYMFLLIVLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNVEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLAGWSSLLSHSPLVLRYIPEGMQCSCGIDYYTLKPEINNESFVIYMFVVHFAIPMIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSDFGPIFMTLPAFFAKSSSIYNPVIYIMMNKQFRNCMITTLCCGKNPLGDDEASASASKTETSQVAPA")
]
data2 = [
    Animal(
        name='Petirrojo europeo (Erithacus rubecula)',
        descripcion="vaca",
        urlImage='./img/petirrojo1.png',
        proteina = "Cry4",
        fasta = ">ATE87950.1 cryptochrome 4 [Erithacus rubecula] MLHRTIHLFRKELRLHDNPVLLAALQSSEALYPVYILDRAFLTSSMHIGALRWHFLLQSLEDLHKNLCQLGSCLLVIQGEYETVLRDHIQKWSITQVTLDAEMEPFYKEMEANIQCLGAELGFEVLSLGSHSLYDTQRILDINGGSPPLTYKRFLHILSLLGDPEVPVRNLTAEDFQRCSAPDPDLAECYRVPLPVDLKISPENLSPWRGGETEGLQRLEQHLTDQGWVASFTKPRTIPNSLLPSTTGLSPYFSMGCLSVRTFFYRLSNIYAQAKHHSLPPVSLQGQLLWREFFYTVASATPNFTQMAGNPICLQICWYKDAERLHKWKMAQTGFPWIDAIMTQLRQEGWIHHLARHAVACFLTRGDLWISWEEGMKVFEELLLDADYSINAGNWMWLSASAFFHQYTRIFCPVRFGKRTDPQGNYIRKYLPILKNFPSKYIYEPWTASEEEQKQAGCIIGRDYPFPMVNHKEASDHNLQLMRQVREEQHRTAQLTRDDADDPMEIKVKRDHTEENISKGKVARTTE"),
    Animal(
        name='Gorrión común (Passer domesticus)',
        descripcion="gorrion",
        urlImage='./img/gorrion1.png',
        proteina = "Cry4",
        fasta = ">AAS72903.1 cryptochrome 4, partial [Passer domesticus]KGLRLHDNPVLLAALESSEALYPVYILDRAFLTSSMHIGALRWNFLLQSLEDLHKNLGQLGSCLLVIQGEYEIVLRDHIQKWNITQVTLDAEMEPFYKEMEANIQRLGVELGFEVFSLVSHSLYNTQRILDLNGGSPPLTYKRFLHILSLLGDPEVPVRNVTAEDFQRCRAPDPGLAECYRVPLPVDLKISPESLSPWRGGETEGLQRLERHLTDQGWVTSFTKPRTVPNSLLPSTTGLSPYFSMGCLSVRTFFYRLSNIYAQAKHHSLPPVSLQGQLLWREFFYTVASATPNFTQMAGNPICLQICWYKDAERLHKWKTAQTGFPWIDAIMTQLRQEGWIHHLARHAVACFLTRGDLW"
    ),
     Animal(
        name='Paloma Bravía (Columba livia)',
        descripcion="paloma",
        urlImage='./img/paloma1.png',
        proteina = "Cry4",
        fasta = ">ANT47196.1 cryptochrome 4 [Columba livia] MPHRTIHLFRKGLRLHDNPTLLAALESSETIYPVYVLDRRFLASAMHIGALRWHFLLQSLEDLHKNLSRLGARLLVIQGEYECVLRDHVQKWNITQVTLDAEMEPFYKEMEANIRRLGAELGFEVLSRVGHSLYDTKRILDLNGGSPPLTYKRFLHILSQLGDPEVPVRNLTAEDFQRCMSPEPGLAERYRVPVPADLEIPPQSLSPWTGGETEGLRRLEQHLTDQGWVANFTKPRTIPNSLLPSTTGLSPYFSMGCLSVRTFFHRLSNIYAQAKHHSLPPVSLQGQLLWREFFYTVASATQNFTQMAGNPICLQIHWYEDAERLHKWKTAQTGFPWIDAIMTQLRQEGWIHHLARHAVACFLTRGDLWISWEEGMKVFEELLLDADYSINAGNWMWLSASAFFHHYTRIFCPVRFGKRTDPEGQYIRKYLPVLKNFPTKYIYEPWTASEEEQRQAGCIIGRDYPFPMVNHKEASDRNLQLMRRVREEQRGTAQLTRDDADDPMEMKRDCSEENTARGKVARGRE"),
      Animal(
        name='Gallo Bankiva (Gallus gallus)',
        descripcion="gallo",
        urlImage='./img/gallo1.png',
        proteina = "Cry4",
        fasta = ">NP_001034685.1 cryptochrome 4 [Gallus gallus] MRHRTIHLFRKGLRLHDNPALLAALQSSEVVYPVYILDRAFMTSSMHIGALRWHFLLQSLEDLRSSLRQLGSCLLVIQGEYESVVRDHVQKWNITQVTLDAEMEPFYKEMEANIRGLGEELGFQVLSLMGHSLYNTQRILELNGGTPPLTYKRFLRILSLLGDPEVPVRNPTAEDFQRCSPPELGLAECYGVPLPTDLKIPPESISPWRGGESEGLQRLEQHLADQGWVASFTKPKTVPNSLLPSTTGLSPYFSTGCLSVRSFFYRLSNIYAQAKHHSLPPVSLQGQLLWREFFYTVASATPNFTKMAGNPICLQIRWYEDAERLHKWKTAQTGFPWIDAIMTQLRQEGWIHHLARHAAACFLTRGDLWISWEEGMKVFEELLLDADYSINAGNWMWLSASAFFHHYTRIFCPVRFGRRTDPEGQYIRKYLPILKNFPSKYIYEPWTASEEEQKQAGCIIGRDYPFPMVDHKEASDHNLQLMKQAREEQHRIAQLTRDDADDPMEMKLKRDHSEESFTKTKAARMTEQT"),
      Animal(
        name='Curruca Mosquitera  (Sylvia borin)',
        descripcion="ave",
        urlImage='./img/sylvia1.png',
        proteina = "Cry4",
        fasta = ">NP_001034685.1 cryptochrome 4 [Gallus gallus] MRHRTIHLFRKGLRLHDNPALLAALQSSEVVYPVYILDRAFMTSSMHIGALRWHFLLQSLEDLRSSLRQLGSCLLVIQGEYESVVRDHVQKWNITQVTLDAEMEPFYKEMEANIRGLGEELGFQVLSLMGHSLYNTQRILELNGGTPPLTYKRFLRILSLLGDPEVPVRNPTAEDFQRCSPPELGLAECYGVPLPTDLKIPPESISPWRGGESEGLQRLEQHLADQGWVASFTKPKTVPNSLLPSTTGLSPYFSTGCLSVRSFFYRLSNIYAQAKHHSLPPVSLQGQLLWREFFYTVASATPNFTKMAGNPICLQIRWYEDAERLHKWKTAQTGFPWIDAIMTQLRQEGWIHHLARHAAACFLTRGDLWISWEEGMKVFEELLLDADYSINAGNWMWLSASAFFHHYTRIFCPVRFGRRTDPEGQYIRKYLPILKNFPSKYIYEPWTASEEEQKQAGCIIGRDYPFPMVDHKEASDHNLQLMKQAREEQHRIAQLTRDDADDPMEMKLKRDHSEESFTKTKAARMTEQT"),      
]
 
Cetaceos = [
    Animal(
        name="Vaquita Marina",
        descripcion="vaca",
        urlImage='./img/vacaMarina.png',
        proteina = "Tmie",
        fasta = ">XP_019802190.1 PREDICTED: transmembrane inner ear expressed protein [Tursiops truncatus] MGMVLRRHLLWPLPSLLCFPVVITLCCVFNCRVPRTRKEIEARYLQRKAAKIYTDKLETVPPLDELTEVPGGDKKKKKKDSVDTVAIKVEEDEKNEAKKKKEEK"
        ),
    Animal(
        name='Delfin Nariz de Botella',
        descripcion="delfinBot",
        urlImage='./img/botella.png',
        proteina = "Tmie",
        fasta = ">XP_004283908.1 PREDICTED: transmembrane inner ear expressed protein [Orcinus orca] MAGQRLGAGPLWALGGAALGVCLAGVAGQLVEPSTAPPKPKPPPLTKETVVFWDMRLWHVVGIFSLFVLSIIITLCCVFNCRVPRTRKEIEARYLQRKAAKIYTDKLETVPPLDELTEVPGGDKKKKKKDSVDTVAIKVEEDEKNEAKKKKEEK"
    ),
     Animal(
        name='Orca',
        descripcion="orca",
        urlImage='./img/orca.png',
        proteina = "Tmie",
        fasta = ">XP_007168911.1 PREDICTED: transmembrane inner ear expressed protein [Balaenoptera acutorostrata scammoni] MAGQRLGAGPLWALGGGAALGVCLAGVAGQLVEPSTAPPKPKPPPLTKETVVFWDMRLWHVVGIFSLFVLSIIITLCCVFNCRVPRTRKEIEARYLQRKAAKMYTDKLETVPPLNELTEIPGEDKKKKKKKDSVDTVAIKVEEDEKNEAKKKKEEK"),
      Animal(
        name='Ballena Minke',
        descripcion="BallenasMinke",
        urlImage='./img/minke.png',
        proteina = "Tmie",
        fasta = ">XP_007126150.2 transmembrane inner ear expressed protein [Physeter catodon] MMPTRSLPATRSPPPSAGWPGGSHRAKAARQASLGSPDLLPSCAERAKMAGQRLGAGPLWALGGAALGVCLAGVAGQLVEPSTAPPKPKPPPLTKETVVFWDMRLWHVVGIFSLFVLSIIITLCCVFNCRVPRTRKEIEARYLQRKAAKMYTDKLETVPPLNELTEIPGEGKKKKKKDSVDTVAIKVEEDEKNEAKKKKEGK"),
      Animal(
        name='Cachalote',
        descripcion="Cachalote",
        urlImage='./img/cachalote.png',
        proteina = "Tmie",
        fasta = ">XP_010765930.1 PREDICTED: transmembrane inner ear expressed protein [Notothenia coriiceps] MFGDQPVCPSQPLLRGALLLSQCLSSVFSQVPDPELLPTDPPKKPDPITSESVVFWGLRLWQVIAIFSVFVLAIIITLCCIFKCRIPRTKKEIEARNVQRQAAKKYANTLETVPPLNELTEIPGSAPDASAVQTVSEQVQTQSATGSQLSIVRVSEEQPGSLTLPETG"),              
]

insectos = [
    Animal(
        name="Garrapata",
        descripcion="Garrapata",
        urlImage='./img/garrapata.png',
        proteina = "Cytochrome",
        fasta = ">ATI15533.1 cytochrome oxidase subunit I, partial (mitochondrion) [Amblyomma dissimile]QPGTLIGNDQIYNVIVTAHAFIMIFFMVMPIMIGGFGNWLVPIMLGAPDMAFPRMNNMSFWLLPPSLCLLINSSLVESGAGTGWTVYPPLSSNLSHYGPSVDMAIFSLHLAGASSILGSINFITTIINMRSIGMTMERIPLFVWSVLTTTILLLLSLPVLAGAITMLLTDRNFN"),
    Animal(
        name='Escorpion',
        descripcion="Escorpion",
        urlImage='./img/escorpion.png',
        proteina = "Cytochrome",
        fasta = ">ADK41046.1 cytochrome oxidase subunit 1, partial (mitochondrion) [Scorpiones sp. BOLD:AAI5611]GDDQIYNVVVTAHAFVMIFFMVMPVMIGGFGNWLVPLMLGAPDMAFPRLNNMSFWLLPPAFFMLLGSAALESGAGTGWTVYPPLSSYMFHSGGSVDMTIFSLHLAGVSSILGAINFITTILNMRSYGMLLERVPLFVWSVKITAILLLLSLPVLAGAITMLLTDRNFNTSFFDPAGGG"),
     Animal(
        name='Arana',
        descripcion="Arana",
        urlImage='./img/arana2.png',
        proteina = "Cytochrome",
        fasta = ">BBG56591.1 cytochrome c oxidase subunit 1, partial (mitochondrion) [Araneae sp. SK-2016]KDIGTLYLVFGAWAAMVGTAMSVLIRIELGQTGSFMGDDQLYNVIVTAHAFVMIFFMVMPILIGGFGNWLVPLMLGAPDMAFPRMNNLSFWLLPPSLLLLFISSMVEMGVGAGWTVYPPLSSLDGHGGSSVDFAIFSLHLAGASSIMGAVNFISTVLNMRSYGMSMEKVPLFVWSVLITAVLLLLSLPVLAGAITMLLTDRNFNTSFFDPAGGGDPILFQHLFWFFGH"),
      Animal(
        name='Alacran',
        descripcion="alacran",
        urlImage='./img/alacran.png',
        proteina = "Cytochrome",
        fasta = ">ALD10489.1 cytochrome c oxidase subunit I, partial (mitochondrion) [Bothriurus flavidus]TMYLILGGWASMVGTALSLLIRAELGSPGSFIGDDQIYNVIVTAHAFVMIFFMVMPVMIGGFGNWLVPLMLGAPDMAFPRLNNMSFWLLPPAFFLLLGSASLESGAGTGWTVYPPLSSYMFHSGGSVDMTIFSLHLAGVSSILGAINFITTIINMRSEGLLLERMPLFVWSVSVTAVLLLLSLPVLAGAITMLLTDRNFNTSFFDPAGGGDPILYQHLFWFFGHPEVYILILPGFGMVSHVISHHTGKKEPFGALGMVYALVAIGFLGFVVWAHHMFTVMDVDTRAYFTAATMVIAVPTGIKIFSWLATIHGSYFDYSPPLLWALGFVFLFTVGGLTGVILANSSLDIVLHDTYYVVA"),
      Animal(
        name='Tarantula Cebra de Costa',
        descripcion="Tarantula",
        urlImage='./img/tarantula.png',
        proteina = "Cytochrome",
        fasta = ">AEL96831.1 cytochrome oxidase subunit I, partial (mitochondrion) [Aphonopelma seemanni]AMSVIIRVELGQVGSLLGDDHLYNVIVTAHALVMIFFMVMPILIGGFGNWMLPLMLGAPDMAFPRMNNLSFWLLPPSLFLLILSSLTDVGVGAGWTIYPPLSSFVGHSGGGMDFAIFSLHLAGASSIMGSVNFISTILNMRGMGMSMDRVPLFVWSVLVTTVLLLLSLPVLAGAITMLLSDRNFNTSFFDPAGGGDPVLFQHLFWFFGHPEVYILILPGFGMISHIISSSVGKREVFGSLGMIYAMVSIGGMGFVVWAHHMFSVGMDVDTRAYFTAATMVIAVPTGIKVFSWMATLYGSYFSMDVSLMWCVGFVFLFTMGG"),              
]

class PestañaAnalisis(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root , width = 800 , height = 600 )
        self.root = root
        self.config(bg = grisOscuro)
        self.pack()

        self.title = tk.Label(self, text = 'Analsis Proteico')
        self.title.config(anchor = tk.CENTER, pady= 20, bg = grisOscuro, font= 1, fg = 'white', width = 80)
        self.title.place(x = 0 , y = 0)

        self.title2 = tk.Label(self, text = "Especies :")
        self.title2.config(anchor =tk.W ,pady= 15, bg = grisOscuro, font= 1, fg = 'white', width = 80)
        self.title2.place(x = 10 , y = 35)

        self.title3 = tk.Label(self, text = "Animales :")
        self.title3.config(anchor=tk.W ,pady= 15, bg = grisOscuro, font= 1, fg = 'white', width = 50)
        self.title3.place(x = 10 , y = 205)

        self.title4 = tk.Label(self, text = "Codigo Fasta :")
        self.title4.config(anchor=tk.CENTER ,pady= 15, bg = grisOscuro, font= 1, fg = 'white', width = 50)
        self.title4.place(x = 270 , y = 205)

        """ MODIFICAR ESTE ARRAY SIMPLE CON UNA ARRAY DE OBJETOS ANIMALES """
        self.listBox = ListBox(self,w = 26, h = 20 ,px=43,py=250)
        #self.fasta = 
        self.caninos = ClaseAnalisis(
            root = self,
            file = './img/mastin.png',
            text = 'Caninos',
            x = 55,
            y = 80,
            data = data,
        )
        
        self.aracnidos = ClaseAnalisis(
            root = self,
            file = './img/arana.png',
            text = 'Aracnidos',
            x = 255,
            y = 80,
            data = insectos,
        )

        self.aves = ClaseAnalisis(
            root = self,
            file = './img/loros.png',
            text = 'Aves',
            x = 455,
            y = 80,
            data = data2,
        )
        
        self.pez = ClaseAnalisis(
            root = self,
            file = './img/pez.png',
            text = 'Cetaceos',
            x = 655,
            y = 80,
            data = Cetaceos,
        )

        self.detalles = detallesA(root = self)

        #self.arbol = tk.Button(self, text = 'Arbol')
        #self.arbol.place(x = 150, y = 540)
        #self.arbol.bind('<Button-1>', lambda e: root.handleBackDetalles(e))

        self.alineamiento = Boton(root = self,text="Alineamiento", x = 150,y = 540)
        self.arbol = Boton(root = self,text = "Arbol", x = 450,y = 540)

    def handleClickImage(self,e,data):
        self.listBox.delete(0,tk.END)
        self.listBox.data = data
        for element in data:
            self.listBox.insert(tk.END,element.name)
    
    def handleListBoxSelect(self,e,data):
        index = self.listBox.curselection()[0]
        self.detalles.nom(objeto= data[index])
        self.detalles.setDescription(objeto= data[index])
        self.detalles.place(x = 245, y = 250)
        self.arbol.proteina = data[index].proteina        

    def handleBackDetalles(self,e):
        self.detalles.place_forget()

    def imprime(self,e,proteina):
        arbol = Arbol(proteina = proteina)
