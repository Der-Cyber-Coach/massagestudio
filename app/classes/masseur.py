import os 
import psycopg2



class masseur:
    """Klasse Masseur: Datenbankobjekt, dass Masseure abfragt, erstellt und löscht
    """    
     
    
    def __init__(self) -> None:
        try:
            self.db = psycopg2.connect(database='massagestudio',host='localhost', user='postgres', password='password', port='9988')
            print("Datenbankverbindung hergestellt")
        except:
            print("Keine DB-Verbindung hergestellt")
    
    def search(self, name: str):
        """Sucht nach einem bestimmten Masseur

        Args:
            name (str): Name des Masseurs

        Returns:
            _type_: Liste mit den gefundenen Masseuren
        """        
        self.cursor = self.db.cursor()
        self.cursor.execute(f"SELECT * FROM masseure WHERE MA_NAME = '{name}';")
        result = self.cursor.fetchall()
        self.cursor.close()
        return result
        
    def create(self, name:str):
        '''Erstellt einen neuen Masseur'''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(f"INSERT INTO masseure ('MA_NAME') VALUES ('{name}');")
            self.cursor.commit()
            print("Masseur erstellt")
            self.cursor.close()
        except:
            print("Masseur konnte nicht erstellt werden")
        self.cursor.close()
        
            
        
    
        
        
            

if __name__=='__main__':
    
    masseur = masseur()
    masseur.search('Hans')
    masseur.create('Hans')
    
