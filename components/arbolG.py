
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

class Arbol():
    def __init__(self,proteina=""):
        self.proteina = proteina
        
        if self.proteina == "Cytochrome":
            with open("./fasta/aracnidos/arac.aln", "r") as aln: 
                alignment = AlignIO.read(aln, "clustal")
        
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(alignment)
        #print(dm)
            constructor = DistanceTreeConstructor(calculator) 
            upgma_tree = constructor.build_tree(alignment)
            Phylo.draw(upgma_tree)

        if self.proteina == "Rodopsina":
            with open("./fasta/canes/canis.aln", "r") as aln: 
                alignment = AlignIO.read(aln, "clustal")
        
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(alignment)
        #print(dm)
            constructor = DistanceTreeConstructor(calculator) 
            upgma_tree = constructor.build_tree(alignment)
            Phylo.draw(upgma_tree)    

        if self.proteina == "Cry4":
            with open("./fasta/aves/cry4.aln", "r") as aln: 
                alignment = AlignIO.read(aln, "clustal")
        
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(alignment)
        #print(dm)
            constructor = DistanceTreeConstructor(calculator) 
            upgma_tree = constructor.build_tree(alignment)
            Phylo.draw(upgma_tree)

        if self.proteina == "Tmie":
            with open("./fasta/cetaceos/tmie.aln", "r") as aln: 
                alignment = AlignIO.read(aln, "clustal")
        
            calculator = DistanceCalculator('identity')
            dm = calculator.get_distance(alignment)
        #print(dm)
            constructor = DistanceTreeConstructor(calculator) 
            upgma_tree = constructor.build_tree(alignment)
            Phylo.draw(upgma_tree)    