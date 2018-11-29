import subprocess
from Bio.Align.Applications import MuscleCommandline

#muscle = "muscle3.8.31_i86linux64"
class alinear():
    def __init__(self):

        self.cline = MuscleCommandline(input ="alinear.fasta",out="arbol.aln",clw=True)
        self.string = str(self.cline)
        subprocess.call(self.string, shell=True)