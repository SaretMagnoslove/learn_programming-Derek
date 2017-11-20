import sqlite3


def printDB():
    try:
        result = theCursor.execute(
            "SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")

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

theCursor = db_conn.cursor()
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT\
                     NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT\
                     NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
except sqlite3.OperationalError:
    print('Probably Exists')

db_conn.execute('INSERT INTO Employees (Fname, LName, Age, Address, Salary, HireDate)'
                'VALUES ("Rene","Matista",34,"Ral St.", 5000, date("now"))')
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                "VALUES ('Derek', 'Banas', 41, '123 Main St', '500,000', date('now'))")
db_conn.commit()

printDB()

try:
    theCursor.execute('UPDATE Employees SET Age = 33 WHERE ID=1')
    db_conn.commit()
except:
    print("could't update table")

printDB()

try:
    theCursor.execute('DELETE FROM Employees WHERE id=1')
    db_conn.commit()
except:
    print("couldn't delete from table")

printDB()

db_conn.rollback()

try:
    theCursor.execute('ALTER TABLE Employees ADD COLUMN "Image" BLOB DEFAULT NULL')
    db_conn.commit()
except:
    print("couldn't add column to table")

theCursor.execute('PRAGMA TABLE_INFO(Employees)')
rownams = [nameTuple[1] for nameTuple in theCursor.fetchall()]
print(rownams)

theCursor.execute('SELECT COUNT(*) FROM Employees')

numOfRows = theCursor.fetchall()
print ("Total number of rows is: ",numOfRows[0][0])

theCursor.execute('SELECT SQLITE_VERSION()')
print("SQLite Version is: ", theCursor.fetchone())

with db_conn:
    db_conn.row_factory = sqlite3.Row
    theCursor = db_conn.cursor()
    theCursor.execute('SELECT * FROM Employees')
    rows = theCursor.fetchall()
    for row in rows:
        print("{}{}".format(row['FName'], row['LName']))

with open('dump.sql','w') as f:
    for line in db_conn.iterdump():
        f.write("%s\n" % line)

db_conn.close()
print('Database closed')
