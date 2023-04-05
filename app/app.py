import tkinter
import classes


def main():
    root = tkinter.Tk()
    root.title("Massagestudio")
    root.geometry("800x600")
    root.resizable(False, False)
    masseur = classes.masseur()
    name = 'Hans'
    suche = masseur.search(name)
    button_masseure = tkinter.Button(root, text="Masseure", command=suche)
    button_masseure.pack()
    
    root.mainloop()
    
    # Ein Button Masseure wird angelegt, beim Klicken soll die Funktion masseur.search aufgerufen werden
    # masseur.search soll eine Liste aller Masseure ausgeben
    # Die Liste soll in einem neuen Fenster angezeigt werden
    list = masseur.search(name)
    
   
if __name__=='__main__':
    main()