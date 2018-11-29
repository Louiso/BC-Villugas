
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

class Arbol():
    def __init__(self,proteina=""):
        self.proteina = proteina

        #if proteina != "":
        with open("./arbol.aln", "r") as aln: 
            alignment = AlignIO.read(aln, "clustal")
        
        calculator = DistanceCalculator('identity')
        dm = calculator.get_distance(alignment)
            #print(dm)
        constructor = DistanceTreeConstructor(calculator) 
        upgma_tree = constructor.build_tree(alignment)
        Phylo.draw(upgma_tree)    