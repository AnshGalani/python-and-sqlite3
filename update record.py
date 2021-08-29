import sqlite3

#connecting to sqlite
conn=sqlite3.connect('test.db')

#creating a cursor object using the cursor() method
cursor=conn.cursor()

#preparing sql queries to update into database.
cursor.execute('''update student set name='ramdas' where id=3''')

#commit your changes in the database
conn.commit()
print("Record update...!")

#closing the connection
conn.close()
