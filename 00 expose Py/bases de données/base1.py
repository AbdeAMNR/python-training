import pyodbc
import matplotlib.pyplot as plt
import pandas as pd  # this is how I usually import pandas
import sys  # only needed to determine Python version number
import matplotlib
from pandas import DataFrame, read_csv

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\med\Desktop\base\base_python.accdb;'
)
db = pyodbc.connect(conn_str)
cursor = db.cursor()
sql = "select note from examen e,etudiant et ,matiere m \
where e.refetudiant=et.cne \
and e.refmatiere=m.idmatiere \
and et.cne= %d " % (123)
l = []

# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
    l.append(row[0])
    # Now print fetched result
# print(l)

df = pd.DataFrame(data=l, columns=['Note'])
Sorted = df.sort_values(['Note'], ascending=False)
print(Sorted)
m = df['Note'].max()
print(m)
# print(df.dtypes)
df['Note'].plot()
plt.show()

# disconnect from server
db.close()
