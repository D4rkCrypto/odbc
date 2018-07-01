# import sys
# import time
# import pyodbc
from flask import Flask, request, render_template

# class DBHelper():
#     def __init__(self):
#         self.conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Ansi Driver};SERVER=127.0.0.1;DATABASE=test;UID=root;PWD=test123!;charset=utf8')
#         self.c = self.conn.cursor()
#         self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER,name VARCHAR(50),gender INTEGER,branch INTEGER,year INTEGER,academic_year INTEGER,address VARCHAR(50),mobile VARCHAR(50))")
#         self.c.execute("CREATE TABLE IF NOT EXISTS payments(reciept_no INTEGER,roll INTEGER,fee INTEGER,semester INTEGER,reciept_date VARCHAR(50))")
#         self.data = []
#         self.list = []

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='127.0.0.1')
