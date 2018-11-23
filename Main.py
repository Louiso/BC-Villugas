import tkinter as tk
from tkinter import ttk
from components.PestañaAnimal import PestañaAnimal

root = tk.Tk()
root.title("Ciro de MRD ... te voy a sacar la MRD")

windows = ttk.Notebook(root)
windows.pack(fill = 'both', expand = 'yes')

pestañaProteinas = PestañaAnimal(root = root)
pestañaAnalisis = PestañaAnimal(root = root)


windows.add(PestañaAnimal(root = root), text = "Animales")
windows.add(pestañaProteinas, text = "Proteinas")
windows.add(pestañaAnalisis, text = 'Analisis')

root.mainloop()
