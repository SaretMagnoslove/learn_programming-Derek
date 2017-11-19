import sqlite3
import sys
import csv

# ---------- FUNCTIONS ----------

def printDB():
    # To retrieve data from a table use SELECT followed
    # by the items to retrieve and the table to
    # retrieve from

    try:
        result = theCurser.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")

        # You receive a list of lists that hold the result
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")

db_conn = sqlite3.connect('test.db')

print('Database Created')

theCurser = db_conn.cursor()
db_conn.commit()

db_conn.execute('DROP TABLE IF EXISTS Employees')
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT\
                     NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT\
                     NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
except sqlite3.OperationalError:
    print('Ooops, An Operational Error Occured')

db_conn.execute('INSERT INTO Employees (Fname, LName, Age, Address, Salary, HireDate)'
                'VALUES ("Rene","Matista",34,"Ral St.", 5000, date("now"))')
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                "VALUES ('Derek', 'Banas', 41, '123 Main St', '500,000', date('now'))")
db_conn.commit() 

printDB() 

db_conn.close()
print('Database closed')