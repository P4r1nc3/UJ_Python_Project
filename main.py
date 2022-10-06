from tkinter import *

class DatabaseConnector:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Database")
        self.root.resizable(width = True, height = True)


if __name__ == '__main__':
    root = Tk()
    application = DatabaseConnector(root)
    root.mainloop()