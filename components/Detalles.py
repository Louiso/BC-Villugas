import tkinter as tk

class Detalles(tk.Frame):
    def __init__(self, root = None, text = 'Vacio'):
        super().__init__(root)

        self.label = tk.Label(self, text = 'Detalles')
        self.label.config(anchor = tk.CENTER, pady= 10, bg = 'gray', width = 35)
        self.label.pack(side = tk.TOP)

        self.body = tk.Frame(self)
        self.body.config(width = 248, height = 244)
        self.body.pack( side = tk.BOTTOM )
        self.descripcion = tk.Text(self.body)
        self.descripcion.insert(tk.INSERT,text)

        self.descripcion.config(width = 35, height = 18)
        self.descripcion.place(x = 0, y = 0)

        self.button = tk.Button(self.body, text = 'Back')
        self.button.place(x = 100, y = 210)
        self.button.bind('<Button-1>', lambda e: root.handleBackDetalles(e))

    def setDescription(self,text = ''):
        self.descripcion.delete('1.0',tk.END)
        self.descripcion.insert(tk.INSERT,text)