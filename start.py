#Program pomocniczy, który pomagal w testowaniu glownego programu
import random
import pymysql

# ========= !IMPORTANT ==========
# ===== Enter your password =====
password = "admin12345"

def generateCar():
    # ===== Choosing random make & model =====
    vehicles = {
        'Ford': ['Focus', 'Mondeo', 'Fiesta'],
        'Audi': ['A1', 'A2', 'A3', 'TT', 'E-tron', 'R8', 'Q3', 'Q5', 'Q7'],
        'Renault': ['Clio', 'Captur', 'Kadjar', 'Zoe', 'Arkana', 'Megane', 'Koleos', 'Express'],
        'Nissan': ['Micra', 'Juke', 'Quasqai', 'GTR', 'Leaf', 'Navara', 'Ariya', 'X-trail'],
        'Toyota': ['Corolla', 'Yaris', 'Auris'],
        'Volkswagen': ['Passat', 'Golf', 'Tiguan', 'Up', 'Polo', 'T-cross', 'Touran', 'Arteon'],
        'BMW': ['3 Series', '5 Series', '1 Series'],
        'Mercedes': ['C-Class', 'E-Class', 'S-Class'],
        'Fiat': ['Panda', '500', 'Punto']
    }

    make = random.choice(list(vehicles.keys()))
    model = random.choice(vehicles[make])

    # ====== Colour ======
    colourList = ['White', 'Black', 'Blue', 'Red', 'Purple', 'Grey', 'Orange', 'Green']
    colour = random.choice(colourList)

    # ===== Year =====
    year = random.randint(1980, 2020)

    # ===== Mileage =====
    mileage = random.randint(0, 200000)

    # ===== Type =====
    body_types = {
        'Focus': 'Hatchback',
        'Mondeo': 'Sedan',
        'Fiesta': 'Hatchback',
        'A1': 'Hatchback',
        'A2': 'Hatchback',
        'A3': 'Sedan',
        'TT': 'Coupe',
        'E-tron': 'SUV',
        'R8': 'Sport Car',
        'Q3': 'SUV',
        'Q5': 'SUV',
        'Q7': 'SUV',
        'Clio': 'Hatchback',
        'Captur': 'SUV',
        'Kadjar': 'SUV',
        'Zoe': 'Hatchback',
        'Arkana': 'Crossover',
        'Megane': 'Hatchback',
        'Koleos': 'SUV',
        'Express': 'Van',
        'Micra': 'Hatchback',
        'Juke': 'SUV',
        'Quasqai': 'SUV',
        'GTR': 'Sport Car',
        'Leaf': 'Hatchback',
        'Navara': 'Pickup Truck',
        'Ariya': 'SUV',
        'X-trail': 'SUV',
        'Corolla': 'Sedan',
        'Yaris': 'Hatchback',
        'Auris': 'Hatchback',
        'Passat': 'Sedan',
        'Golf': 'Hatchback',
        'Tiguan': 'SUV',
        'Up': 'Hatchback',
        'Polo': 'Hatchback',
        'T-cross': 'SUV',
        'Touran': 'Minivan',
        'Arteon': 'Fastback',
        '3 Series': 'Sedan',
        '5 Series': 'Sedan',
        '1 Series': 'Hatchback',
        'C-Class': 'Sedan',
        'E-Class': 'Sedan',
        'S-Class': 'Sedan',
        'Panda': 'Hatchback',
        '500': 'Hatchback',
        'Punto': 'Hatchback'
    }

    type = body_types[model]

    return make, model, colour, year, mileage, type

def createDataBase(x):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host="localhost", user="root", password=x)
        cursor = sqlConnection.cursor()
        cursor.execute('CREATE DATABASE carDataBase')
        sqlConnection.commit()
    except pymysql.err.ProgrammingError:
        print("Error: Taka Baza danych juz istnieje")
    except pymysql.err.InternalError:
        print("Error: Nie masz uprawnien do utworzenia bazy danych")
    finally:
        if sqlConnection:
            sqlConnection.close()

def createTable(x):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
        cursor = sqlConnection.cursor() 
        cursor.execute('CREATE TABLE car (id int(11) NOT NULL auto_increment, make VARCHAR(64) NOT NULL, model VARCHAR(64) NOT NULL, colour VARCHAR(64) NOT NULL, year int(11), mileage int(11), type VARCHAR(64) NOT NULL, PRIMARY KEY (id))')
        sqlConnection.commit()
    except pymysql.err.OperationalError as e:
        print(f"Wystapil blad: {e}")
    finally:
        if sqlConnection:
            sqlConnection.close()

def insertRecords(x, size):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
        cursor = sqlConnection.cursor()
        for i in range(0, size):
            cursor.execute('insert into car (make, model, colour, year, mileage, type) values' + str(generateCar()))
        sqlConnection.commit()
    except pymysql.err.OperationalError as e:
        print(f"Wystapil blad: {e}")
    finally:
        if sqlConnection:
            sqlConnection.close()

def removeDataBase(x):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
        cursor = sqlConnection.cursor()
        cursor.execute("DROP DATABASE carDataBase")
        sqlConnection.commit()
    except pymysql.err.OperationalError:
        print("Error: Baza danych nie istnieje")
    finally:
        if sqlConnection:
            sqlConnection.close()

def showDataBase(x):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
        cursor = sqlConnection.cursor()
        cursor.execute("select * from car;")
        result = cursor.fetchall()
        for row in result:
            print(row)
            print("\n")
        sqlConnection.commit()
    except pymysql.err.OperationalError as e:
        print(f"Wystapil blad: {e}")
    finally:
        if sqlConnection:
            sqlConnection.close()


def removeAllRecords(x):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host="localhost", user="root", password=x, database="carDataBase")
        cursor = sqlConnection.cursor()
        cursor.execute("DELETE FROM car")
        sqlConnection.commit()
    except pymysql.err.OperationalError as e:
        print(f"Wystapil blad: {e}")
    finally:
        if sqlConnection:
            sqlConnection.close()

def checkPassword(password):
    sqlConnection = None
    try:
        sqlConnection = pymysql.connect(host='localhost', user="root", password=password)
        return True
    except pymysql.MySQLError:
        return False
    finally:
        if sqlConnection:
            sqlConnection.close()

if __name__ == '__main__':
    while True:
        # Checking if the password is correct
        isValid = checkPassword(password)

        if isValid:
            print("  Jaka czynnosc chcesz wykonac?")
        else:
            print("Haslo jest niepoprawne")
            break
        
        print("1-Utworzyc baze danych wraz z tabela")
        print("2-Wgrac przykladowe rekordy do bazy danych")
        print("3-Usunac baze danych")
        print("4-Wyswietlic wszystkie rekordy")
        print("5-Usunac wszystkie rekordy")
        print("0-Wyjscie")
        choice = int(input("  Wprowadz swoj wybor: "))
        print("==========================================")

        if choice == 1:
            createDataBase(password)
            createTable(password)
        elif choice == 2:
            size = int(input("  Ile rekordow mam wgrac?: "))
            insertRecords(password, size)
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