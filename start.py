#Program pomocniczy, który pomagal w testowaniu glownego programu
import pymysql

def createDataBase(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x)
    cursor = sqlConnection.cursor()
    cursor.execute('CREATE DATABASE carDataBase')
    sqlConnection.commit()
    sqlConnection.close()

def createTable(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    cursor.execute('CREATE TABLE car (id int(11) NOT NULL auto_increment, make VARCHAR(64), model VARCHAR(64), colour VARCHAR(64), year VARCHAR(64), type VARCHAR(64), PRIMARY KEY (id))')
    sqlConnection.commit()
    sqlConnection.close()

def insertRecords(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    cursor.execute('insert into car (make, model, colour, year, type) values("Audi", "A8", "White", "2020", "Coupe")')
    cursor.execute('insert into car (make, model, colour, year, type) values("Ford", "Ranger Raptor", "Blue", "2018", "Pickup Truck")')
    cursor.execute('insert into car (make, model, colour, year, type) values("BMW", "Series 1", "Black", "2012", "Hatchback")')
    cursor.execute('insert into car (make, model, colour, year, type) values("Renault", "Clio", "Red", "2016", "Hatchback")')
    cursor.execute('insert into car (make, model, colour, year, type) values("Ferrari", "Enzo", "Red", "2002", "Sport Car")')
    cursor.execute('insert into car (make, model, colour, year, type) values("Volkswagen", "Passat", "Black", "2010", "Sedan")')
    cursor.execute('insert into car (make, model, colour, year, type) values("Nissan", "Juke", "Grey", "2022", "SUV")')
    sqlConnection.commit()
    sqlConnection.close()

def removeDataBase(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    cursor.execute("DROP DATABASE carDataBase")
    sqlConnection.commit()
    sqlConnection.close()

def showDataBase(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    cursor.execute("select * from car;")
    result = cursor.fetchall()
    for row in result:
        print(row)
        print("\n")

    sqlConnection.commit()
    sqlConnection.close()

def removeAllRecords(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    cursor.execute("DELETE FROM car")
    sqlConnection.commit()
    sqlConnection.close()

if __name__ == '__main__':
    password = input("Podaj haslo do profilu root mysql: ")

    while True:
        print("  Jaka czynnosc chcesz wykonac?")
        print("1-Utworzyc baze danych wraz z tabela")
        print("2-Wgrac przykladowe rekordy do bazy danych")
        print("3-Usunac baze danych")
        print("4-Wyswietlic wszystkie rekordy")
        print("5-Usunac wszystkie rekordy")
        print("0-Wyjscie")
        choice = int(input("  Wprowadz swoj wybor: "))

        if choice == 1:
            createDataBase(password)
            createTable(password)
        elif choice == 2:
            insertRecords(password)
        elif choice == 3:
            removeDataBase(password)
        elif choice == 4:
            showDataBase(password)
        elif choice == 5:
            removeAllRecords(password)
        elif choice == 0:
            break
        else:
            print("Wprowadzono nie poprawny numer. Sprobuj ponownie.")

    print("  Do zobaczenia!")