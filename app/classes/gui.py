import tkinter

from .masseur import *
from .patienten import *
from .raum import *
 

class view(raum):
     
    def __init__(self):
        super().__init__()
        schema = 'massagestudio'
        self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
        
    
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
        self.ausgabevariable = tkinter.StringVar()
        return self.root
        
    def raum(self):
        self.raum = tkinter.Tk()
        self.raum.title("Raum")
        self.raum.geometry("800x600")
        self.raum.resizable(False, False)
        self.raum.configure(bg="white")
        return self.raum
    
    def masseure(self):
        
        self.masseur= masseur()
        # Fensterkonfiguration
        self.masseure = tkinter.Toplevel()
        self.masseure.title("Masseure")
        self.masseure.geometry("800x600")
        self.masseure.resizable(False, False)
        self.masseure.configure(bg="white")
        self.eingabevariable = tkinter.StringVar()
       
        
        
        # Button funktionen: Funktionen müssen definiert werden, damit sie beim Klicken aufgerufen werden können
        def eingabe_erstellen():#
           # self.ausgabevariable = f"Der Masseur {self.eingabevariable.get()} wird erstellt"
            Entry = tkinter.Entry(self.masseure, textvariable=self.eingabevariable)
            Entry.pack()
            def masseur_erstellen():
                if self.eingabevariable.get() == "":
                    
                    self.ausgabevariable = "Bitte einen Namen eingeben"
                    label = tkinter.Label(self.masseure, text=self.ausgabevariable)
                    label.pack()
                    
                elif self.eingabevariable.get() != "":
                    self.ausgabevariable = f"Der Masseur {self.eingabevariable.get()} wird erstellt"
                    label = tkinter.Label(self.masseure, text=self.ausgabevariable)
                    label.pack(side="right")
                    #self.ausgabevariable.configure(text=self.ausgabevariable)
                    self.masseur.create(self.eingabevariable.get())
                    self.eingabevariable.set("")
            self.button_ERSTELLEN = tkinter.Button(self.masseure, text="Masseur erstellen", command=masseur_erstellen)
            self.button_ERSTELLEN.pack()
            
            
        def masseur_löschen():
            self.masseur_löschen = self.masseur.delete('Test')
        def masseur_ändern():
            self.masseur_ändern = self.masseur.update('Test', 'Test2')
        def masseur_suchen():
            self.masseur_suchen = self.masseur.search('Test')
            
        # Buttons
        self.button_masseur_erstellen = tkinter.Button(self.masseure, text="Masseur erstellen", command=eingabe_erstellen)
        self.button_masseur_löschen = tkinter.Button(self.masseure, text="Masseur löschen", command=masseur_löschen)
        self.button_masseur_ändern = tkinter.Button(self.masseure, text="Masseur ändern", command=masseur_ändern)
        self.button_masseur_suchen = tkinter.Button(self.masseure, text="Masseur suchen", command=masseur_suchen)
        
        
        
        # Buttons packen
        self.button_masseur_löschen.pack()
        self.button_masseur_ändern.pack()
        self.button_masseur_suchen.pack()
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
 
 