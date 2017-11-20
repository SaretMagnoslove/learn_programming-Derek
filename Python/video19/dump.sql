BEGIN TRANSACTION;
CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT                     NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT                     NOT NULL, Address TEXT, Salary REAL, HireDate TEXT, "Image" BLOB DEFAULT NULL);
INSERT INTO "Employees" VALUES(2,'Derek','Banas',41,'123 Main St','500,000','2017-11-19',NULL);
INSERT INTO "Employees" VALUES(3,'Rene','Matista',34,'Ral St.',5000.0,'2017-11-19',NULL);
INSERT INTO "Employees" VALUES(4,'Derek','Banas',41,'123 Main St','500,000','2017-11-19',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Employees',4);
COMMIT;
