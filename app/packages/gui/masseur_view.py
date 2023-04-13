import tkinter
from .actions import * 

class masseur_gui:
    def __init__(self) -> None:
        pass
    
    
    
    
    def root(self):
        self.root = tkinter.Tk()
        self.root.title("Masseuere verwalten")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.root.mainloop()
    
    def buttons(self):
        self.button_add = tkinter.Button(self.root, text="Masseur hinzufügen", command= masseur_add)
        self.button_delete = tkinter.Button(self.root, text="Masseur löschen", command= masseur_delete)
        self.button_edit = tkinter.Button(self.root, text="Masseur bearbeiten", command=masseur_edit)
        self.button_add.pack()
        self.button_delete.pack()
        self.button_edit.pack()