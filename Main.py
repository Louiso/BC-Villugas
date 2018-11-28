import tkinter as tk
from tkinter import ttk
from pestañas.PestañaAnimal import PestañaAnimal
from pestañas.PestañaProteinas import PestañaProteinas
from pestañas.PestañaAnalisis import PestañaAnalisis
 
root = tk.Tk()
root.title("Biologia Computacional")

windows = ttk.Notebook(root)
windows.pack(fill = 'both', expand = 'yes')

pestañaProteinas = PestañaProteinas(root = root)
pestañaAnalisis = PestañaAnalisis(root = root)


windows.add(PestañaAnimal(root = root), text = "Animales")
windows.add(pestañaProteinas, text = "Proteinas")
windows.add(pestañaAnalisis, text = 'Analisis')

root.mainloop()
