import os 
import psycopg2



class masseur:
    """Klasse Masseur: Datenbankobjekt, dass Masseure abfragt, erstellt und löscht
    """    
     
    
    def __init__(self) -> None:
        try:
            schema = 'massagestudio'
            self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
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
      #  self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988')       
        self.cursor = self.db.cursor()
      #  self.cursor.execute(f"SET search_path TO massagestudio;")
        self.cursor.execute(f"SELECT * FROM masseure WHERE MA_NAME = '{name}';")
        result = self.cursor.fetchall()
        self.cursor.close()
        print (result)
        
    def create(self, name:str):
        '''Erstellt einen neuen Masseur'''
        

        self.cursor = self.db.cursor()
        
        try:
            self.cursor.execute(f"INSERT INTO masseure(MA_NAME) VALUES ('{name}');")
            self.db.commit()
            print(f"Masseur {name} erstellt")
        except:
            print(f"Der Masseur mit dem Namen {name} konnte nicht erstellt werden")
            self.cursor.close()
            
    def update(self, name_neu:str, name_alt:str):
        '''Ändert einen Masseur'''
        
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute(f"UPDATE masseure SET MA_NAME = '{name_neu}' WHERE MA_NAME = '{name_alt}';")
            print(f"Masseur {name_alt} wurde zu {name_alt} geändert")
        except:
            print(f"Der Masseur mit dem Namen {name} konnte nicht geändert werden")
            self.cursor.close()
            
    def delete(self, name:str):
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute(f"DELETE FROM masseure WHERE MA_NAME = '{name}';")
            print(f"Masseur {name} gelöscht")
        except:
            print(f"Der Masseur mit dem Namen {name} konnte nicht gelöscht werden")
            self.cursor.close()
            
            
            
        
            
        
    
        
        
            

if __name__=='__main__':
    
    masseur = masseur()
    masseur.search('Hans')
    masseur.create("Jürgen Wurst")
    masseur.update("Jürgen Wurst", "Jürgen Muster")
    masseur.delete("Jürgen Wurst")
    
    
