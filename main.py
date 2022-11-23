# ========================= Importing Libraries =========================
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import pymysql
import sys


# ========================= Enter Your Password for root User =========================
pswd = "admin12345"

# ========================= General =========================
root = Tk()
root.title("Car Database")
root.resizable(width=False, height=False)

# ========================= Variables =========================
carMake = StringVar()
carModel = StringVar()
carColour = StringVar()
carYear = StringVar()
carType = StringVar()
carMileage = StringVar()

# ========================= Frames =========================
# Main Frame
MainFrame = Frame(root, bd=20, width=1000, height=1000, relief=RIDGE, bg='black')
MainFrame.grid()

# Left Frame
LeftFrame = Frame(MainFrame, bd=6, relief=RIDGE)
LeftFrame.pack(side=LEFT)

LeftFrame0 = Frame(LeftFrame, bd=2, relief=RIDGE)
LeftFrame0.pack(side=TOP, pady=0, padx=0)

# Right Frame
RightFrame = Frame(MainFrame, bd=5, relief=RIDGE)
RightFrame.pack(side=RIGHT)

# ========================= Labels & Entry =========================
# Car Make
lblCarMake = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Car Make", bd=8)
lblCarMake.grid(row=0, column=0, sticky=W, padx=50)

entryCarMake = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left',
                     textvariable=carMake)
entryCarMake.grid(row=0, column=1, sticky=W, padx=50)

# Car Model
lblCarModel = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Car Model", bd=8)
lblCarModel.grid(row=1, column=0, sticky=W, padx=50)

entryCarModel = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left',
                     textvariable=carModel)
entryCarModel.grid(row=1, column=1, sticky=W, padx=50)

# Car Colour
lblCarColour = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Car Colour", bd=8)
lblCarColour.grid(row=2, column=0, sticky=W, padx=50)

entryCarColour = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left',
                     textvariable=carColour)
entryCarColour.grid(row=2, column=1, sticky=W, padx=50)

# Car Production Year
lblProductionYear = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Car Production Year", bd=8)
lblProductionYear.grid(row=3, column=0, sticky=W, padx=50)

entryProductionYear = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left',
                     textvariable=carYear)
entryProductionYear.grid(row=3, column=1, sticky=W, padx=50)

# Car Mileage
lblMileage = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Car Mileage", bd=8)
lblMileage.grid(row=4, column=0, sticky=W, padx=50)

entryMileage = Entry(LeftFrame0, font=('arial', 12, 'bold'), bd=8, width=40, justify='left',
                     textvariable=carMileage)
entryMileage.grid(row=4, column=1, sticky=W, padx=50)

# Car Body Type
lblBodyType = Label(LeftFrame0, font=('arial', 12, 'bold'), text="Car Body Type", bd=8)
lblBodyType.grid(row=5, column=0, sticky=W, padx=50)

boxBodyType = ttk.Combobox(LeftFrame0, textvariable=carType)
boxBodyType['values'] = (' ', 'Sedan', 'Coupe', 'Sport Car', 'Station Wagon', 'Hatchback',
                              'Convertible', 'SUV', 'Minivan', 'Pickup Truck', 'Different')
boxBodyType.current(0)
boxBodyType.grid(row=5, column=1, sticky=W, padx=50)


# ======================== Commands ========================
def exit():
    EXIT = tkinter.messagebox.askyesno("Car Database", "Are You sure You want to exit?")
    if EXIT > 0:
        root.destroy
        sys.exit(0)

def reset():
    entryCarMake.delete(0, END)
    entryCarModel.delete(0, END)
    entryProductionYear.delete(0, END)
    entryCarColour.delete(0, END)
    entryMileage.delete(0, END)
    boxBodyType.set(" ")

def addNew():
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()

    Make = carMake.get()
    Model = carModel.get()
    Colour = carColour.get()
    Year = carYear.get()
    Mileage = carMileage.get()
    Type = carType.get()

    if Make == "" or Model == "" or Colour == "" or Year == "" or Mileage == "" or Type == " ":
        tkinter.messagebox.showinfo("Car Database", "Make sure to enter all values!")
    else:
        insert_query = "INSERT INTO car (make, model, colour, year, mileage, type) VALUES(%s, %s, %s, %s, %s, %s)"
        values = (Make, Model, Colour, Year, Mileage, Type)
        cur.execute(insert_query, values)
        sqlConnection.commit()
        incrementReset()
        tkinter.messagebox.showinfo("Car Database", "Record Entered Successfully!")
        display()
    sqlConnection.close()

def display():
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()
    insert_query = "SELECT * FROM car"
    cur.execute(insert_query)
    result = cur.fetchall()
    if len(result) != 0:
        record.delete(*record.get_children())
        for row in result:
            record.insert('', END, values=row)
        sqlConnection.commit()
    sqlConnection.close()

def delete():
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()

    viewInfo = record.focus()
    learnerData = record.item(viewInfo)
    row = learnerData['values']

    insert_query = "DELETE FROM car WHERE id=%s"
    cur.execute(insert_query, row[0])
    sqlConnection.commit()
    sqlConnection.close()
    incrementReset()
    display()
    tkinter.messagebox.showinfo("Car Database", "Record Deleted Successfully!")

def incrementReset():
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()
    cur.execute("CREATE TABLE new_car AS SELECT id, make, model, colour, year, mileage, type FROM car")
    cur.execute("DELETE FROM car")
    cur.execute("ALTER TABLE car AUTO_INCREMENT = 1")
    cur.execute("INSERT INTO car (make, model, colour, year, mileage, type) SELECT make, model, colour, year, mileage, type FROM new_car ORDER BY id ASC")
    cur.execute("DROP TABLE new_car")
    sqlConnection.commit()
    sqlConnection.close()

def info(event):
    # checks the region we click (we can take data only from normal cell)
    region = record.identify("region", event.x, event.y)
    if region == "cell":
        viewInfo = record.focus()
        learnerData = record.item(viewInfo)
        row = learnerData['values']
        carMake.set(row[1])
        carModel.set(row[2])
        carColour.set(row[3])
        carYear.set(row[4])
        carMileage.set(row[5])
        carType.set(row[6])

def update():
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()

    Make = carMake.get()
    Model = carModel.get()
    Colour = carColour.get()
    Year = carYear.get()
    Mileage = carMileage.get()
    Type = carType.get()

    viewInfo = record.focus()
    learnerData = record.item(viewInfo)
    row = learnerData['values']

    insert_query = "UPDATE car SET make=%s, model=%s, colour=%s, year=%s, mileage=%s, type=%s WHERE id=%s"
    values = (Make, Model, Colour, Year, Mileage, Type, row[0])
    cur.execute(insert_query, values)

    sqlConnection.commit()
    display()
    sqlConnection.close()
    tkinter.messagebox.showinfo("Car Database", "Record Updated Successfully!")

def search():
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()

    Make = carMake.get()
    Model = carModel.get()
    Colour = carColour.get()
    Year = carYear.get()
    Mileage = carMileage.get()
    Type = carType.get()

    counter = 0
    values = []
    insert_query = "SELECT * FROM car WHERE %s LIKE '%s'"
    insert_query_count = "SELECT COUNT(*) FROM car WHERE %s LIKE '%s'"

    if Make != '' or Model != '' or Colour != '' or Year != '' or Mileage != '' or Type != ' ':
        if Make != '':
            values.append("make")
            values.append(Make)
            counter += 1
        if Model != '':
            values.append("model")
            values.append(Model)
            counter += 1
        if Colour != '':
            values.append("colour")
            values.append(Colour)
            counter += 1
        if Year != '':
            values.append("year")
            values.append(Year)
            counter += 1
        if Mileage != '':
            values.append("mileage")
            values.append(Mileage)
            counter += 1
        if Type != ' ':
            values.append("type")
            values.append(Type)
            counter += 1

        values = tuple(values)

        if counter == 1:
            sql1 = (insert_query %values)
            sql2 = (insert_query_count % values)
        else:
            for i in range(0, counter - 1):
                insert_query += " AND %s LIKE '%s'"
                insert_query_count += " AND %s LIKE '%s'"
            sql1 = (insert_query %values)
            sql2 = (insert_query_count % values)

        cur.execute(sql2)
        amount = cur.fetchone()[0]
        cur.execute(sql1)
        result = cur.fetchall()
        if len(result) != 0:
            record.delete(*record.get_children())
            for row in result:
                record.insert('', END, values=row)
            sqlConnection.commit()
        tkinter.messagebox.showinfo("Car Database", "Found %s records matching the criteria" % amount)
    sqlConnection.close()

def sorting(filter, count):
    if count % 2 == 1:
        sortingASC(filter)
    else:
        sortingDESC(filter)

def sortingASC(filter):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()

    cur.execute("create table sorted as select * from car order by %s" %filter)
    insert_query = "SELECT * FROM sorted"
    cur.execute(insert_query)
    result = cur.fetchall()
    if len(result) != 0:
        record.delete(*record.get_children())
        for row in result:
            record.insert('', END, values=row)
        sqlConnection.commit()
    cur.execute(" drop table sorted")
    sqlConnection.commit()
    sqlConnection.close()

def sortingDESC(filter):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=pswd, database="carDataBase")
    cur = sqlConnection.cursor()

    cur.execute("CREATE TABLE sorted AS SELECT * FROM car ORDER BY %s DESC" %filter)
    insert_query = "SELECT * FROM sorted"
    cur.execute(insert_query)
    result = cur.fetchall()
    if len(result) != 0:
        record.delete(*record.get_children())
        for row in result:
            record.insert('', END, values=row)
        sqlConnection.commit()
    cur.execute("DROP TABLE sorted")
    sqlConnection.commit()
    sqlConnection.close()

count = 0
def OnDoubleClick(event):
    column = record.identify_column(event.x)
    region = record.identify("region", event.x, event.y)

    global count
    count += 1

    if region == "heading" and column == "#1":
        sorting("id", count)
    elif region == "heading" and column == "#2":
        sorting("make", count)
    elif region == "heading" and column == "#3":
        sorting("model", count)
    elif region == "heading" and column == "#4":
        sorting("colour", count)
    elif region == "heading" and column == "#5":
        sorting("year", count)
    elif region == "heading" and column == "#6":
        sorting("mileage", count)
    elif region == "heading" and column == "#7":
        sorting("type", count)

# ========================= Scrollbar =========================
scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)

columns = ('id', 'make', 'model', 'colour', 'year', 'mileage', 'type')
record = ttk.Treeview(LeftFrame, height=12, columns=columns, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)

record.heading('id', text='ID')
record.heading('make', text='Make')
record.heading('model', text='Model')
record.heading('colour', text='Colour')
record.heading('year', text='Production Year')
record.heading('mileage', text='Mileage')
record.heading('type', text='Body Type')

record['show'] = 'headings'

record.column('id', width=50)
record.column('make', width=90)
record.column('model', width=90)
record.column('colour', width=90)
record.column('year', width=90)
record.column('mileage', width=90)
record.column('type', width=90)

record.pack(fill=BOTH, expand=1)
record.bind("<ButtonRelease-1>", info)
record.bind("<Double-1>", OnDoubleClick)
display()
# ========================= Buttons =========================
# ADD BUTTON
btnAddNew = Button(RightFrame, font=('arial', 12, 'bold'), text="Add New",
                        bd=8, pady=2, padx=20, width=10, height=3, command=addNew)
btnAddNew.grid(row=0, column=0, padx=5)

# UPDATE BUTTON
btnUpdate = Button(RightFrame, font=('arial', 12, 'bold'), text="Update",
                        bd=8, pady=2, padx=20, width=10, height=3, command=update)
btnUpdate.grid(row=1, column=0, padx=5)

# DISPLAY BUTTON
btnDisplay = Button(RightFrame, font=('arial', 12, 'bold'), text="Display",
                         bd=8, pady=2, padx=20, width=10, height=3, command=display)
btnDisplay.grid(row=2, column=0, padx=5)

# DELETE BUTTON
btnDelete = Button(RightFrame, font=('arial', 12, 'bold'), text="Delete",
                        bd=8, pady=2, padx=20, width=10, height=3, command=delete)
btnDelete.grid(row=3, column=0, padx=5)

# SEARCH BUTTON
btnSearch = Button(RightFrame, font=('arial', 12, 'bold'), text="Search",
                        bd=8, pady=2, padx=20, width=10, height=3, command=search)
btnSearch.grid(row=4, column=0, padx=5)

# RESET BUTTON
btnReset = Button(RightFrame, font=('arial', 12, 'bold'), text="Reset",
                       bd=8, pady=2, padx=20, width=10, height=3, command=reset)
btnReset.grid(row=5, column=0, padx=5)

# EXIT BUTTON
btnExit = Button(RightFrame, font=('arial', 12, 'bold'), text="Exit",
                      bd=8, pady=2, padx=20, width=10, height=3, command=exit)
btnExit.grid(row=6, column=0, padx=5)

if __name__ == '__main__':
    root.mainloop()