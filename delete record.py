import sqlite3

#connecting to sqlite3
conn=sqlite3.connect('test.db')

#creating a cursor object using the cursor() method
cursor=conn.cursor()

#preparing sql queries to insert a record into the database
cursor.execute('''delete from student where id=3''')

#commit your changes in the database
conn.commit()
print("Record delete...!")

#closing the connection
conn.close()
