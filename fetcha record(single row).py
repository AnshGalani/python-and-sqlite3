import sqlite3

try:
    connection=sqlite3.connect('test.db')
    cursor=connection.cursor()
    print("Connection to database")

    query="select*from student"
    cursor.execute(query)
    print("Fetching singal row")
    record=cursor.fetchone()
    print(record)

    print("Fetching next row")
    record=cursor.fetchone()
    print(record)

    cursor.close()

except sqlite3.Error as error:
    print("Failes to read data from tables",error)

finally:
    if connection:
        connection.close()
        print("The sqlite connection is closed")
