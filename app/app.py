import tkinter
import classes


def main():
    root = tkinter.Tk()
    root.title("Massagestudio")
    root.geometry("800x600")
    root.resizable(False, False)
    masseur = classes.masseur()
    name = 'Hans'
    suche_masseur = masseur.search(name)
    patient = classes.patienten()
    suche_patient = patient.search(name)
    button_masseure = tkinter.Button(root, text="Masseure suchen", command=suche_masseur)
    button_masseure.pack()
    button_patientensuche = tkinter.Button(root,text="Patientensuche",command=suche_patient)
    button_patientensuche.pack()
    
    root.mainloop()
    
    # Ein Button Masseure wird angelegt, beim Klicken soll die Funktion masseur.search aufgerufen werden
    # masseur.search soll eine Liste aller Masseure ausgeben
    # Die Liste soll in einem neuen Fenster angezeigt werden
    list = masseur.search(name)
    
   
if __name__=='__main__':
    main()