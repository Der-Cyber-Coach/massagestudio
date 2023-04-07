import tkinter

from .masseur import *
from .patienten import *
from .raum import *
 

class view(masseur,patienten):
     
    def __init__(self):
        super().__init__()
        
    
    def root(self):
        self.root = tkinter.Tk()
        self.root.title("Massagestudio")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        button_raum = tkinter.Button(self.root, text="Raumverwaltung", command=self.raum)
        button_Masseure = tkinter.Button(self.root, text="Masseurverwaltung",command=self.masseure)
        button_Patienten = tkinter.Button(self.root, text="Patientenverwaltung",command=self.patienten)
        buttton_termine = tkinter.Button(self.root, text="Terminbuchung",command=self.termine)
        button_alleslöschen = tkinter.Button(self.root, text="Alles löschen",command=self.alleslöschen)
        button_Masseure.pack()
        button_Patienten.pack()
        buttton_termine.pack()
        button_alleslöschen.pack()
        button_raum.pack()
        self.root.configure(bg="white")
        return self.root
        
    def raum(self):
        self.raum = tkinter.Toplevel()
        self.raum.title("Raum")
        self.raum.geometry("800x600")
        self.raum.resizable(False, False)
        self.raum.configure(bg="white")
        return self.raum
    
    def masseure(self):
        
        # Fensterkonfiguration
        self.masseure = tkinter.Toplevel()
        self.masseure.title("Masseure")
        self.masseure.geometry("800x600")
        self.masseure.resizable(False, False)
        self.masseure.configure(bg="white")
        
        
        
        # Buttons
        self.button_masseur_erstellen = tkinter.Button(self.masseure, text="Masseur erstellen")
        self.button.masseur_löschen = tkinter.Button(self.masseure, text="Masseur löschen", command=self.masseur_löschen)
        self.button.masseur_ändern = tkinter.Button(self.masseure, text="Masseur ändern", command=self.masseur_ändern)
        self.button.masseur_suchen = tkinter.Button(self.masseure, text="Masseur suchen", command=self.masseur_suchen)
        self.button.zurück = tkinter.Button(self.masseure, text="Zurück", command=self.root)
        
        
        
        self.button_masseur_erstellen.pack()
        return self.masseure
    
    
    
    
    def patienten(self):
        self.patienten = tkinter.Toplevel()
        self.patienten.title("Patienten")
        self.patienten.geometry("800x600")
        self.patienten.resizable(False, False)
        self.patienten.configure(bg="white")
        return self.patienten
    def termine(self):
        self.termine = tkinter.Toplevel()
        self.termine.title("Termine")
        self.termine.geometry("800x600")
        self.termine.resizable(False, False)
        self.termine.configure(bg="white")
        return self.termine
    
    def alleslöschen(self):
        self.alleslöschen = tkinter.Toplevel()
        self.alleslöschen.title("Alles löschen")
        self.alleslöschen.geometry("800x600")
        self.alleslöschen.resizable(False, False)
        self.alleslöschen.configure(bg="white")
        return self.alleslöschen
 
 