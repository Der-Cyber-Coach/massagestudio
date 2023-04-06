import psycopg2
import os

class patienten:
    '''Klasse, die ein Patientenobjekt erstellt'''
    def __init__(self) -> None:
        try:
            schema = 'massagestudio'
            self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
            print("200 OK")
        except:
            self.db.close()
            print("500 Datenbankverbindung gescheitert")
            os._exit(1)
    
    # Patientensuche
    
    def search(self,name:str,patientennummer:int):
        '''Suche nach einem Patienten'''
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * from patienten WHERE pa_id= {patientennummer} AND pa_name = '{name}';")
            result = self.cursor.fetchall()
            print(result)
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Der Patient mit der Patientennummer: {patientennummer} und dem Namen: {name} konnte nicht gefunden werden.")
            os._exit(1)
    
    
       
    def create(self, name:str):
        """Erstellt einen Patienten und fügt in in die Datenbank ein

        Args:
            name (str): Vor- und Nachname des Patienten
        """        
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute(f"INSERT INTO patienten(pa_name) VALUES ('{name}');")
            print(f"Der Patient {name} wurde in die Patientendatei aufgenommen.")
            self.db.commit()
            self.cursor.close()
        except:
            print(f"Fehler, der Patient {name} wurde nicht aufgenommen.")
            self.cursor.close()
            self.db.close()
            os._exit(1)
    
                
    
    def update(self, name_alt:str, name_neu: str):
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute(f"UPDATE patienten SET pa_name = '{name_neu}' WHERE pa_name = '{name_alt}';")
            print(f"Der Name des Patienten {name_alt} wurde zu {name_neu} geändert;")
            self.db.commit()
            self.cursor.close()
            self.db.close()
        except:
            print(f"Fehler, der Name des Patienten {name_alt} konnte nicht zu {name_neu} geändert werden.")
            self.cursor.close()
            self.db.close()
            os._exit(1)
            
    
    def delete(self,patientennummer:int):
        """Löscht einen Patienten anhand der Patientennummer

        Args:
            patientennummer (int): Nummer des Patienten. Suche benutzen um sie herauszufinden.
        """        
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute(f"DELETE FROM patienten WHERE pa_id = {patientennummer};")
            print(f"Patient mit der  Patientennummer {patientennummer} wurde gelöscht.")
            self.db.commit()
            self.cursor.close()
            self.db.close()
        except:
            print(f"Der Patient mit der Patientennummer {patientennummer} konnte leider nicht gelöscht werden.")
            self.cursor.close()
            self.db.close()
            os._exit(1)
    
            
    
    







if __name__=='__main__':
    patient = patienten()
    patient.search('Hans',1)
    patient.create('Jens')
    patient.search('Jens',2)
    patient.delete(2)
            

