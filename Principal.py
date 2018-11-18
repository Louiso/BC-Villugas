from tkinter import *
# import Secuencia
import time
root=Tk()
root.title("PRINCIPAL")
#miFrame=Frame(raiz)
miFrame=Frame(root,width="700",height="1200")
miFrame.config(cursor="spider",bg="green") #Configuración del marco

miFrame.pack()

def  mostrar():
   lst1.place(x=290,y=150)
   boton6.place(x=310,y=340)	   


def  mostrar2():
   lst2.place(x=290,y=150)

def  mostrar3():
   lst3.place(x=290,y=150)
def  mostrar4():
   lst4.place(x=290,y=150)


def f(indice,root):
    if indice == 0:
       root.iconify()

       root=Tk()
       root.title("CANINOS")
       #miFrame=Frame(raiz)
       miFrame=Frame(root,width="700",height="1200")
       miFrame.config(cursor="spider",bg="blue") #Configuración del marco
       miFrame.pack()
       time.sleep(5) 
    if indice == 1:
       root.iconify()
       root=Tk()
       root.title("CANINOS")
       #miFrame=Frame(raiz)
       miFrame=Frame(root,width="700",height="1200")
       miFrame.config(cursor="spider",bg="yellow") #Configuración del marco
       miFrame.pack()
    if indice == 2:
       root.iconify()
       root=Tk()
       root.title("CANINOS")
       #miFrame=Frame(raiz)
       miFrame=Frame(root,width="700",height="1200")
       miFrame.config(cursor="spider",bg="blue") #Configuración del marco
       miFrame.pack()
    #time.sleep(5)
      
    #root.deiconify()

      
""" Maneja el evento de seleccionar elemento de lista """

#tmi=m1.subsample(4,4)
#boton1.config(image=tmi)
boton1=Button(miFrame,text="CANINOS",command=mostrar)
m1=PhotoImage(file="mastin.png")
boton1.config(image=m1,compound=RIGHT)
tmi=m1.subsample(4,4)
boton1.config(image=tmi)
boton1.place(x=100,y=150)

#
boton2=Button(miFrame,text="aves",command=mostrar2)
m2=PhotoImage(file="loros.png")
boton2.config(image=m1,compound=RIGHT)
tmo=m2.subsample(8,8)
boton2.config(image=tmo)
boton2.place(x=100,y=300)
#
boton3=Button(miFrame,text="aracnidos",command=mostrar3)
m3=PhotoImage(file="arana.png")
boton3.config(image=m3,compound=RIGHT)
tmp=m3.subsample(4,4)
boton3.config(image=tmp)
boton3.place(x=500,y=150)

#
boton5=Button(miFrame,text="peces",command=mostrar4)
m4=PhotoImage(file="pez.png")
boton5.config(image=m4,compound=RIGHT)
tma=m4.subsample(9,9)
boton5.config(image=tma)
boton5.place(x=500,y=300)
#boton analisis
boton6=Button(miFrame,text="analisis",width=10,height=3)

lst1=Listbox(miFrame,width=20)
lst1.insert(0,"lobo")
lst1.insert(1,"can")
lst1.insert(2,"asd")
lst1.insert(3,"name 4")

lst2=Listbox(miFrame,width=20)
lst2.insert(0,"paloma")
lst2.insert(1,"aveztrus")
lst2.insert(2,"name 3")
lst2.insert(3,"name 4")

lst3=Listbox(miFrame,width=20)
lst3.insert(0,"araña")
lst3.insert(1,"tarantula")
lst3.insert(2,"name 3")
lst3.insert(3,"name 4")

lst4=Listbox(miFrame,width=20)
lst4.insert(0,"ballena")
lst4.insert(1,"orca")
lst4.insert(2,"bonito")
lst4.insert(3,"name 4")

def handleSelectElementList(event):
    indice = lst1.curselection()[0]
    f(indice,root)

lst1.bind("<<ListboxSelect>>", handleSelectElementList)                  

miFrame.mainloop()