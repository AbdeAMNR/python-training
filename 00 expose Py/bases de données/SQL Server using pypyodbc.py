import pypyodbc

# cnx = pypyodbc.connect('Driver={SQL Server};'
#                        'Server=localhost;'
#                        'Database=testdb;'
#                        'uid=sa;pwd=P@ssw0rd')

cnx = pypyodbc.connect(driver='{SQL Server}', server='localhost', database='demo', trusted_connection='yes')
cursor = cnx.cursor()
SQLCommand = ("INSERT INTO Employees (FullName, idCard) VALUES (?,?)")
Values = ['Susan', 'Ibach']
cursor.execute(SQLCommand, Values)
cnx.commit()

cursor.execute("SELECT * FROM Employees")
my_rows = cursor.fetchall()
try:
    for row in my_rows:
        print(row)
finally:
    cnx.close()