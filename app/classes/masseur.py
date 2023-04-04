import os 
import psycopg2



class masseur:
    """Klasse Masseur: Datenbankobjekt, dass Masseure abfragt, erstellt und löscht
    """    
     
    
    def __init__(self) -> None:
        try:
            db = psycopg2.connect(database='massagestudio',host='localhost', user='postgres', password='password', port='9988')
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
        self.cursor.execute(f"SELECT * FROM masseur WHERE name = '{name}';")
        
        return self.cursor.fetchall()
    
    
        
        
            

if __name__=='__main__':
    test = masseur()
