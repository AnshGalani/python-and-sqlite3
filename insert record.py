import sqlite3

#connecting to sqlite
conn=sqlite3.connect('test.db')

#creating a cursor using cursor() method
cursor=conn.cursor()

#preparing sql queries to insert a record into the database.
cursor.execute('''insert into student(id,name,city) values(1,'ansh','surat')''')

cursor.execute('''insert into student(id,name,city) values(2,'meet','rajkot')''')

cursor.execute('''insert into student(id,name,city) values(3,'vivek','kamrej')''')

cursor.execute('''insert into student(id,name,city) values(4,'kartik','jamnagar')''')

cursor.execute('''insert into student(id,name,city) values(5,'ayushi','surat')''')

cursor.execute('''insert into student(id,name,city) values(6,'nirali','kamrej')''')

#commit your change in the database
conn.commit()
print("Record inserted...!")

#closing the connection
conn.close()
