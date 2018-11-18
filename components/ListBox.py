import tkinter as tk

from helpers.colors import grisClaro

class ListBox(tk.Listbox):
    def __init__(self, root = None, data = []):
        super().__init__(root)
        self.config(
            width = 35,
            height = 20,
            selectbackground = grisClaro,
            relief = tk.FLAT
            )
        self.place(x = 280, y = 160)
        self.data = data
        self.bind('<<ListboxSelect>>', lambda e: root.handleListBoxSelect(e,self.data))
    