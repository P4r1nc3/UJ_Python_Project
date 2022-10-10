import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import pymysql
import sys


class DatabaseConnector:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Database")
        self.root.resizable(width=False, height=False)

        # ======================== Commands ========================
        def exit():
            EXIT = tkinter.messagebox.askyesno("Movie Database", "Are You sure You want to exit?")
            if EXIT > 0:
                root.destroy
                sys.exit(0)

        def reset():
            self.entryMovieName.delete(0, END)
            self.entryDirector.delete(0, END)
            self.entryPremiere.delete(0, END)
            self.entryLength.delete(0, END)
            self.boxGenre.set(" ")

        def addData():
            sqlConnection = pymysql.connect(host="localhost", user="root", password="toor", database="test")
            sqlConnection.commit()
            sqlConnection.close()


        # ========================= Frames =========================
        # Main Frame
        MainFrame = Frame(self.root, bd=20, width=1000, height=1000, relief=RIDGE, bg='black')
        MainFrame.grid()

        # Left Frame
        LeftFrame = Frame(MainFrame, bd=5, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        LeftFrame0 = Frame(LeftFrame, bd=5, relief=RIDGE)
        LeftFrame0.pack(side=TOP, pady=0, padx=0)

        # Right Frame
        RightFrame = Frame(MainFrame, bd=5, relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        # ========================= Labels & Entry =========================
        # Movie Name
        self.lblMovieName = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Movie Title", bd=8)
        self.lblMovieName.grid(row=0, column=0, sticky=W, padx=50)

        self.entryMovieName = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryMovieName.grid(row=0, column=1, sticky=W, padx=50)

        # Movie Director
        self.lblDirector = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Movie Director", bd=8)
        self.lblDirector.grid(row=1, column=0, sticky=W, padx=50)

        self.entryDirector = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryDirector.grid(row=1, column=1, sticky=W, padx=50)

        # Movie Length
        self.lblLength = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Movie Length", bd=8)
        self.lblLength.grid(row=2, column=0, sticky=W, padx=50)

        self.entryLength = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryLength.grid(row=2, column=1, sticky=W, padx=50)

        # Movie Premiere
        self.lblPremiere = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Movie Premiere", bd=8)
        self.lblPremiere.grid(row=3, column=0, sticky=W, padx=50)

        self.entryPremiere = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left')
        self.entryPremiere.grid(row=3, column=1, sticky=W, padx=50)

        # Movie Genre
        self.lblGenre = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Movie Genre", bd=8)
        self.lblGenre.grid(row=4, column=0, sticky=W, padx=50)

        self.boxGenre = ttk.Combobox(LeftFrame0)
        self.boxGenre['values'] = (' ', 'Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror',
                                   'Musical', 'Mystery', 'Romance', 'Sci-FI', 'Thriller')
        self.boxGenre.current(0)
        self.boxGenre.grid(row=4, column=1, sticky=W, padx=50)

        # ========================= Scrollbar =========================
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)

        self.record = ttk.Treeview(LeftFrame, height=10, columns=('name', 'director', 'length', 'premiere', 'genre'),
                                   yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.record.heading('name', text='Movie Name')
        self.record.heading('director', text='Movie Director')
        self.record.heading('length', text='Movie Length')
        self.record.heading('premiere', text='Movie Premiere')
        self.record.heading('genre', text='Movie Genre')

        self.record['show'] = 'headings'

        self.record.column('name', width=100)
        self.record.column('director', width=100)
        self.record.column('length', width=100)
        self.record.column('premiere', width=100)
        self.record.column('genre', width=100)

        self.record.pack(fill=BOTH, expand=1)

        # ========================= Buttons =========================
        self.btnAddNew = Button(RightFrame, font=('arial', 12, 'bold'), text="Add New",
                                bd=8, pady=2, padx=20, width=10, height=3)
        self.btnAddNew.grid(row=0, column=0, padx=5)

        self.btnDisplay = Button(RightFrame, font=('arial', 12, 'bold'), text="Display",
                                 bd=8, pady=2, padx=20, width=10, height=3)
        self.btnDisplay.grid(row=1, column=0, padx=5)

        self.btnUpdate = Button(RightFrame, font=('arial', 12, 'bold'), text="Update",
                                bd=8, pady=2, padx=20, width=10, height=3)
        self.btnUpdate.grid(row=2, column=0, padx=5)

        self.btnDelete = Button(RightFrame, font=('arial', 12, 'bold'), text="Delete",
                                bd=8, pady=2, padx=20, width=10, height=3)
        self.btnDelete.grid(row=3, column=0, padx=5)

        self.btnSearch = Button(RightFrame, font=('arial', 12, 'bold'), text="Search",
                                bd=8, pady=2, padx=20, width=10, height=3)
        self.btnSearch.grid(row=4, column=0, padx=5)

        self.btnReset = Button(RightFrame, font=('arial', 12, 'bold'), text="Reset",
                               bd=8, pady=2, padx=20, width=10, height=3, command=reset)
        self.btnReset.grid(row=5, column=0, padx=5)

        self.btnExit = Button(RightFrame, font=('arial', 12, 'bold'), text="Exit",
                              bd=8, pady=2, padx=20, width=10, height=3, command=exit)
        self.btnExit.grid(row=6, column=0, padx=5)

if __name__ == '__main__':
    root = Tk()
    application = DatabaseConnector(root)
    root.mainloop()