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
            self.cursor.execute(f"SELECT * from patienten WHERE pa_id= {patientennummer} AND pa_name = {name};")
            result = self.cursor.fetchall()
            print(result)
        except:
            self.db.close()
            print(f"Fehler: Der Patient mit der Patientennummer: {patientennummer} und dem Namen: {name} konnte nicht gefunden werden.")
            os._exit(1)
        
    
    
    
    def create(self, name:str):
        pass
    
    
    def update(self, name_alt:str, name_neu: str, patientennummer:int):
        pass
    
    
    
    







if __name__=='__main__':
    patient = patienten()

            

