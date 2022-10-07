from tkinter import *
from tkinter import ttk

class DatabaseConnector:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Database")
        self.root.resizable(width=False, height=False)

        # ========================= Frames =========================
        MainFrame = Frame(self.root, bd=20, width=300, height=500, relief=RIDGE, bg='black')
        MainFrame.grid()

        # ========================= Labels =========================
        self.lblMovieName = Label(MainFrame, font=('arial', 12, 'bold'), text="Movie Title", bd=8)
        self.lblMovieName.grid(row=0, column=0, sticky=W, padx=50)

        self.lblDirector = Label(MainFrame, font=('arial', 12, 'bold'), text="Movie Director", bd=8)
        self.lblDirector.grid(row=1, column=0, sticky=W, padx=50)

        self.lblLength = Label(MainFrame, font=('arial', 12, 'bold'), text="Movie Length", bd=8)
        self.lblLength.grid(row=2, column=0, sticky=W, padx=50)

        self.lblPremiere = Label(MainFrame, font=('arial', 12, 'bold'), text="Movie Premiere", bd=8)
        self.lblPremiere.grid(row=3, column=0, sticky=W, padx=50)

        self.lblGenre = Label(MainFrame, font=('arial', 12, 'bold'), text="Movie Genre", bd=8)
        self.lblGenre.grid(row=4, column=0, sticky=W, padx=50)

        # ========================= Entry =========================
        self.entryMovieName = Entry(MainFrame, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryMovieName.grid(row=0, column=1, sticky=W, padx=50)

        self.entryDirector = Entry(MainFrame, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryDirector.grid(row=1, column=1, sticky=W, padx=50)

        self.entryLength = Entry(MainFrame, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryLength.grid(row=2, column=1, sticky=W, padx=50)

        self.entryPremiere = Entry(MainFrame, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryPremiere.grid(row=3, column=1, sticky=W, padx=50)

        # ========================= Box =========================
        self.boxGenre = ttk.Combobox(MainFrame)
        self.boxGenre['values'] = (' ', 'Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-FI', 'Thriller')
        self.boxGenre.current(0)
        self.boxGenre.grid(row=4, column=1, sticky=W, padx=50)

if __name__ == '__main__':
    root = Tk()
    application = DatabaseConnector(root)
    root.mainloop()