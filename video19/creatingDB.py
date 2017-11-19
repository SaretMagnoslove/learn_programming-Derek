import sqlite3

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
    
db_conn.close()
print('Database closed')