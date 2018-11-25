import tkinter as tk

from helpers.colors import grisClaro

class ListBox(tk.Listbox):
    def __init__(self, root = None, data = []):
        super().__init__(root)
        self.config(
            width = 45,
            height = 30,
            selectbackground = grisClaro,
            relief = tk.FLAT
            )
        self.place(x = 242, y = 120)
        self.data = data
        self.bind('<<ListboxSelect>>', lambda e: root.handleListBoxSelect(e,self.data))
    