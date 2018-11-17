from tkinter import *
from Bio import SeqIO

lista=[]
lista1=[]
lista2=[]
lista3=[]
lista4=[]

cont=0
def insert(txtSecuencia):
    for x in range(0,len(lista)): 
        txtSecuencia.insert(END,lista[x]+"\n")

def cargarFasta(indice):
    def lineaConSaltoDeLinea(linea):
        return linea[-1] == '\n'
    
    if indice == 0:
        
        archivo = open("test.fasta","r")
        linea=archivo.readline()
        lblImagen=Label(miFrame,image=imagenL)
        lblImagen.place(x=100,y=100)

        while linea:
            if lineaConSaltoDeLinea(linea):
                linea=linea[:-1]
                lista.append(linea)
                linea=archivo.readline()
        archivo.close()

        txtSecuencia.place(x=160,y=420)
        insert(txtSecuencia)

    if indice == 1:
         archivo = open("test.fasta","r")
         linea=archivo.readline()
         
         while linea:
             if lineaConSaltoDeLinea(linea):
                 linea=linea[:-1]
                 lista1.append(linea)
                 linea=archivo.readline()
         archivo.close()

         txtSecuencia.place(x=160,y=420)
         insert(txtSecuencia)
    if indice == 2:
         archivo=open("test.fasta","r")
         linea=archivo.readline()
         
         while linea:
             if lineaConSaltoDeLinea(linea):
                 linea=linea[:-1]   
                 lista2.append(linea) 
                 linea=archivo.readline() 
         archivo.close()
         txtSecuencia.place(x=160,y=420)
         insert(txtSecuencia)
    if indice == 3:
        archivo=open("test.fasta","r")
        linea=archivo.readline()
        
        while  linea:
             if lineaConSaltoDeLinea(linea):
                 linea=linea[:-1]
                 lista3.append(linea)
                 linea=archivo.readline()

        archivo.close()
        txtSecuencia.place(x=160,y=420)
        insert(txtSecuencia)    
    if indice == 4:
        archivo=open("test.fasta","r")
        linea=archivo.readline()
        
        while  linea:
             if lineaConSaltoDeLinea(linea):
                 linea=linea[:-1]
                 lista4.append(linea)
                 linea=archivo.readline()
        archivo.close()
        txtSecuencia.place(x=160,y=420)
        insert(txtSecuencia)       
    
root=Tk()
root.title("biologia computacional")
miFrame=Frame(root,width="700",height="1200")
miFrame.pack()

#miFrame.title("biologia computacional")
""" Crea el primer cuadro donde se muestran los animales """
""" Label """
lblMaterias = Label(miFrame,text="secuencias:")
lblMaterias.place(x=10,y=400)
""" Lista """
lstMaterias=Listbox(miFrame,width=20)
lstMaterias.insert(0,"secuencia 1")
lstMaterias.insert(1,"secuencia 2")
lstMaterias.insert(2,"secuencia 3")
lstMaterias.insert(3,"secuencia 4")

""" Eliminando el nodo 2 """
#lstMaterias.delete(2)
lstMaterias.place(x=10,y=420)
#


#



def handleSelectElementList(event):
    """ lstMaterias.get() devuelve el valor dentro de la lista"""
    """ lstMaterias.curselection ... devuelve el indice del elemento seleccionado """
    indice = lstMaterias.curselection()[0]

    cargarFasta(indice)
    
""" Maneja el evento de seleccionar elemento de lista """
lstMaterias.bind("<<ListboxSelect>>", handleSelectElementList)

""" Segundo cuadro donde se muestran los animales """
lblMat = Label(miFrame,text="animal")
lblMat.place(x=150,y=400)

entrada=StringVar()

txtSecuencia=Text(miFrame,height=20,width=550)
txtDescripcion=Text(miFrame,height=20,width=400)
imagenL=PhotoImage(file="Kid_goku_small.png")
miFrame.mainloop()













