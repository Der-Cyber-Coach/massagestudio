import tkinter
import psycopg2


from packages import datamodels
from .raum_view import *

 

class main_root(datamodels.raum):
     
    def __init__(self):
        super().__init__()
        schema = 'massagestudio'
        self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
        
    
    def root(self):
        self.root = tkinter.Tk()
        self.root.title("Massagestudio")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
       
    
    def buttons(self):    
        
        def raum_window_button():
                raum_window = raum_gui()
                raum_window.root()
            
            
            
            
            
        self.button_raum = tkinter.Button(self.root, text="Raumverwaltung", command=raum_window_button)
        #button_Masseure = tkinter.Button(root, text="Masseurverwaltung",command=masseure)
       # button_Patienten = tkinter.Button(root, text="Patientenverwaltung",command=patienten)
       # buttton_termine = tkinter.Button(root, text="Terminbuchung",command=termine)
       # button_alleslöschen = tkinter.Button(root, text="Alles löschen",command=alleslöschen)
      #  button_Masseure.pack()
       # button_Patienten.pack()
      #  buttton_termine.pack()
      #  button_alleslöschen.pack()
        self.button_raum.pack(side="left", padx=10, pady=10)
        
       