import sqlite3

try:
    connection=sqlite3.connect('test.db')
    cursor=connection.cursor()
    print("Connection to database")

    query="select*from student"
    cursor.execute(query)
    print("Fetching All Row")
    record=cursor.fetchall()
    print("Total rows are",len(record))
    print("Printing each row")

    for row in record:
        print("ID:",row[0])
        print("Student Name: ",row[1])

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from tables",error)

finally:
    if connection:
        connection.close()
        print("The sqlite connection is closed")
        
