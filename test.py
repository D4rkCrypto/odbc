import pyodbc

conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Ansi Driver};SERVER=127.0.0.1;DATABASE=test;UID=root;PWD=test123!')
cursor = conn.cursor()
for row in cursor.execute("desc test_tbl"):
    print(row.Field)
