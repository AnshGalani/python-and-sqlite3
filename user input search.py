import sqlite3 as sq
c=sq.connect('D:/SEM-3/Database Handling/data sql test/test.db')

nm=input("Enter student City")

a=c.execute(f"select*from student where city='{nm}'")
for i in a:
    print(i)
