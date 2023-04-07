import psycopg2
from .patienten import *
from .masseur import *

class raum(masseur,patienten):
    def __init__(self) -> None:
        super().__init__()
        schema='massagestudio'
        try:
            self.db = psycopg2.connect(database='postgres',host='localhost', user='postgres', password='password', port='9988',options=f"-c search_path={schema}")
            print("200 OK")
        except:
            print("500 Datenbankverbindung gescheitert")
            self.db.close()
            os._exit(1)
    
    def raumsuche(self,raumnummer:int):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * from raum WHERE ra_id = {raumnummer};")
            result = self.cursor.fetchall()
            print(result)
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Der Raum mit der Nummer: {raumnummer} konnte nicht gefunden werden.")
            os._exit(1)
            
            
    def behandlung_erstellen(self,pa_id:int,ma_id:int,ra_id:int,behandlung:str,datum:str):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"INSERT INTO behandlung (pa_id,ma_id,ra_id,behandlung,datum) VALUES ({pa_id},{ma_id},{ra_id},'{behandlung}','{datum}');")
            print(f"Die Behandlung wurde erfolgreich erstellt.")
            self.db.commit()
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht erstellt werden.")
            os._exit(1)
            
    def behandlung_loeschen(self,pa_id:int,ma_id:int,ra_id:int,behandlung:str,datum:str):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"DELETE FROM behandlung WHERE pa_id = {pa_id} AND ma_id = {ma_id} AND ra_id = {ra_id} AND behandlung = '{behandlung}' AND datum = '{datum}';")
            print(f"Die Behandlung wurde erfolgreich gelöscht.")
            self.db.commit()
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht gelöscht werden.")
            os._exit(1)
            
    def behandlung_aendern(self,pa_id:int,ma_id:int,ra_id:int,behandlung_alt:str,behandlung_neu:str,datum:str):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"UPDATE behandlung SET behandlung = '{behandlung_neu}' WHERE pa_id = {pa_id} AND ma_id = {ma_id} AND ra_id = {ra_id} AND behandlung = '{behandlung_alt}' AND datum = '{datum}';")
            print(f"Die Behandlung wurde erfolgreich geändert.")
            self.db.commit()
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht geändert werden.")
            os._exit(1)
            
    def behandlung_anzeigen(self,pa_id:int,ma_id:int,ra_id:int,behandlung:str,datum:str):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * FROM behandlung WHERE pa_id = {pa_id} AND ma_id = {ma_id} AND ra_id = {ra_id} AND behandlung = '{behandlung}' AND datum = '{datum}';")
            result = self.cursor.fetchall()
            print(result)
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht angezeigt werden.")
            os._exit(1)
            
    def behandlung_anzeigen_alle(self):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * FROM behandlung;")
            result = self.cursor.fetchall()
            print(result)
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht angezeigt werden.")
            os._exit(1)
            
    def behandlung_anzeigen_alle_masseur(self,ma_id:int):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * FROM behandlung WHERE ma_id = {ma_id};")
            result = self.cursor.fetchall()
            print(result)
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht angezeigt werden.")
            os._exit(1)
            
    def behandlung_anzeigen_alle_patient(self,pa_id:int):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * FROM behandlung WHERE pa_id = {pa_id};")
            result = self.cursor.fetchall()
            print(result)
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht angezeigt werden.")
            os._exit(1)
            
    def behandlung_anzeigen_alle_raum(self,ra_id:int):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"SELECT * FROM behandlung WHERE ra_id = {ra_id};")
            result = self.cursor.fetchall()
            print(result)
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Die Behandlung konnte nicht angezeigt werden.")
            os._exit(1)
    
    #Methode, um Termine in 15 Minuten Schritten zu buchen, zwischen 6 und 20 Uhr von Montag bis Freitag    
    def termin(self,pa_id:int,ma_id:int,ra_id:int,behandlung:str,datum:str, uhrzeit:str):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(f"INSERT INTO termin (pa_id,ma_id,ra_id,behandlung,datum,uhrzeit) VALUES ({pa_id},{ma_id},{ra_id},'{behandlung}','{datum}','{uhrzeit}');")
            print(f"Der Termin wurde erfolgreich erstellt.")
            self.db.commit()
            self.cursor.close()
            self.db.close()
        except:
            self.cursor.close()
            self.db.close()
            print(f"Fehler: Der Termin konnte nicht erstellt werden.")
            os._exit(1)
            
        