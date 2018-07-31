import pyodbc
DBfile = r"D:\ZKTeco\ZKTime5.0\att2000.mdb"
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBfile)

cursor = conn.cursor()
SQL = r"SELECT name,ssn FROM userinfo;"
for row in cursor.execute(SQL): # cursors are iterable
     print(row[0],row[1])
cursor.close()
conn.close()