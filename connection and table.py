import sqlite3

from sqlite3 import Error

#this function is used for creating new database

def sql_connection():
    try:
        con=sqlite3.connect('test.db')
        print("Database is established")
        return con
    except Error:
        print(Error)

def sql_table (con):
    cursorObj=con.cursor()
    cursorObj.execute("craete table student (id integer primary key,name text,city text,dob text)")
    print("Table is created")
    con.commit()

    con=sql_connection()
    sql_table(con)
