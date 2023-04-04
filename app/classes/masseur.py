import os 
import psycopg2


class masseur:
    # fragt in der postgresdatenbank massagestudio aus der Tabellle alle masseure ab und speichert sie in einer liste 
    
    def __init__(self) -> None:
        try:
            database = postgres.Postgres()