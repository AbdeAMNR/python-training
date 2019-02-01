import pyodbc

cnxn = pyodbc.connect(driver='{SQL Server}', server='localhost', database='demo', trusted_connection='yes')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Employees")

my_rows = cursor.fetchall()
print(my_rows)
# Method 1
try:
    for row in my_rows:
        print(row)
finally:
    cnxn.close()

# Method 2
# try:
#     for row in range(0,len(my_rows)):
#         print(my_rows[row][1])
# finally:
#     cnxn.close()

# Method 3
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row)
# cnxn.close()
