import tkinter

class termin_gui:
    def __init__(self) -> None:
        pass
    
    
    
    
    def root(self):
        self.root = tkinter.Tk()
        self.root.title("Termin verwalten")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.root.mainloop()