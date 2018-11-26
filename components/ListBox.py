import tkinter as tk

from helpers.colors import grisClaro

class ListBox(tk.Listbox):
    def __init__(self, root = None, data = [],w = 45,h = 30,px = 242,py = 120):
        super().__init__(root)
        self.config(
            #width = 45,
            #height = 30,
            width = w,
            height = h,
            selectbackground = grisClaro,
            relief = tk.FLAT
            )
        self.place(x = px, y = py)
        self.data = data
        self.bind('<<ListboxSelect>>', lambda e: root.handleListBoxSelect(e,self.data))
    