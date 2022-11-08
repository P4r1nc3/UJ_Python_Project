#Program pomocniczy, który pomagal w testowaniu glownego programu
import random
import pymysql

def generateCar():
    # ===== Choosing random make from a list =====
    makeList = ['Bmw', 'Audi', 'Mercedes', 'Renault', 'Volkswagen', 'Nissan']
    make = random.choice(makeList)

    # ===== Choosing random model for proper make =====
    modelBmw = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5', 'Series 6', 'E46']
    modelAudi = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'TT', 'E-tron', 'R8', 'Q3', 'Q5', 'Q7']
    modelMercedes = ['GTR', 'A class', 'B class', 'C class', 'E class', 'S class', 'G class']
    modelRenault = ['Clio', 'Captur', 'Kadjar', 'Zoe', 'Arkana', 'Megane', 'Koleos', 'Express']
    modelVolkswagen = ['Passat', 'Golf', 'Tiguan', 'Up', 'Polo', 'T-cross', 'Touran', 'Arteon']
    modelNissan = ['Micra', 'Juke', 'Quasqai', 'GTR', 'Leaf', 'Navara', 'Ariya', 'X-trail']
    model = ''

    if make == 'Bmw':
        model = random.choice(modelBmw)
    elif make == 'Audi':
        model = random.choice(modelAudi)
    elif make == 'Mercedes':
        model = random.choice(modelMercedes)
    elif make == 'Renault':
        model = random.choice(modelRenault)
    elif make == 'Volkswagen':
        model = random.choice(modelVolkswagen)
    elif make == 'Nissan':
        model = random.choice(modelNissan)
    # ====== Colour ======
    colourList = ['White', 'Black', 'Blue', 'Red', 'Purple', 'Grey', 'Orange', 'Green']
    colour = random.choice(colourList)

    # ===== Year =====
    year = random.randint(2000, 2022)

    # ===== Mileage =====
    mileage = random.randint(1000, 200000    )

    # ===== Type =====
    typeList = ['Sedan', 'Coupe', 'Sport Car', 'Station Wagon', 'Hatchback',
            'Convertible', 'SUV', 'Minivan', 'Pickup Truck', 'Different']
    type = random.choice(typeList)

    return make, model, colour, year, type

def createDataBase(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x)
    cursor = sqlConnection.cursor()
    cursor.execute('CREATE DATABASE carDataBase')
    sqlConnection.commit()
    sqlConnection.close()

def createTable(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    cursor.execute('CREATE TABLE car (id int(11) NOT NULL auto_increment, make VARCHAR(64) NOT NULL, model VARCHAR(64) NOT NULL, colour VARCHAR(64) NOT NULL, year int(11), mileage int(11), type VARCHAR(64) NOT NULL, PRIMARY KEY (id))')
    sqlConnection.commit()
    sqlConnection.close()

def insertRecords(x):
    sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
    cursor = sqlConnection.cursor()
    for i in range(0, 1000):
        cursor.execute('insert into car (make, model, colour, year, type) values' + str(generateCar()))
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
    password = "admin12345"

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