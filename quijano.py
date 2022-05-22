import pyodbc


try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Colleen M. Quijano\Downloads\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('''
                    INSERT INTO Table1 (ID, FullName, Age, SemGrade, Address, Birthdate )
                    VALUES
                    (?,?,?,?,?,?)''',
                    (11,'Colleen M. Quijano', 19, 90, 'Cavite', '11/16/2002'))
    database.commit()

    print("Data Added")

except pyodbc.Error:
    print("Error in Connection")
