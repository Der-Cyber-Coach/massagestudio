# Description: This is the main file for the application. It is the entry point for the application. It imports the view class from the gui module and creates an instance of it. It then calls the root method of the view class to get the root window and calls the mainloop method of the root window to start the application.
import classes


def main():
   view = classes.gui.view()
   root = view.root()
   root.mainloop()





if __name__=='__main__':
    main()