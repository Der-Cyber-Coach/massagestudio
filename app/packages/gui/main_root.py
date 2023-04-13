import tkinter
import psycopg2


from packages import datamodels
from .raum_view import *
from .masseur_view import *
from .patienten_view import *
from .termin_view import *

 

class main_root(datamodels.raum):
     
    def __init__(self):
        super().__init__()
        schema = 'massagestudio'
        self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
        
    
    def root(self):
        self.root = tkinter.Tk()
        self.root.title("Massagestudio")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
       
    
    def buttons(self):    
        
        def raum_window_button():
                raum_window = raum_gui()
                raum_window.root()
            
        def masseure_window_button():
                masseur_window = masseur_gui() 
                masseur_window.root()   
        def patienten_window_button():
                patienten_window = patienten_gui()
                patienten_window.root()
        def termine_window_button():
                termine_window = termin_gui()
                termine_window.root()
            
            
            
        self.button_raum = tkinter.Button(self.root, text="Raumverwaltung", command=raum_window_button)
        self.button_Masseur = tkinter.Button(self.root, text="Masseurverwaltung",command=masseure_window_button)
        self.button_Patienten = tkinter.Button(self.root, text="Patientenverwaltung",command=patienten_window_button)
        self.buttton_termine = tkinter.Button(self.root, text="Terminbuchung",command=termine_window_button)
        self.button_Masseur.pack(side="left", padx=10, pady=10)
        self.button_Patienten.pack(side="left", padx=10, pady=10)
        self.buttton_termine.pack(side = "left", padx=10, pady=10)
        self.button_raum.pack(side="left", padx=10, pady=10)
        
       