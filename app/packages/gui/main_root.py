import tkinter
import psycopg2


from packages import datamodels
from .raum_view import *

 

class main_root(raum):
     
    def __init__(self):
        super().__init__()
        schema = 'massagestudio'
        self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
        self.root = tkinter.Tk()
        self.root.title("Massagestudio")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.raum_view = raum_view()
        button_raum = tkinter.Button(self.root, text="Raumverwaltung", command=self.raum_view)
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
   