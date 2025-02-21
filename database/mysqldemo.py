import mysql.connector

dbcon = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="25novpython"
)

cursor = dbcon.cursor()

# cursor.execute("create database 25novpython")
# cursor.execute("create table student(id int primary key auto_increment,name varchar(20),email varchar(50))")

# cursor.execute("insert into student values(0,'Harsh','Harsh@gmail.com')")
# dbcon.commit()

# data =  cursor.execute("show tables")
# for i in cursor.fetchall():
#     print(i)

cursor.execute("select * from student")
for i in cursor.fetchall():
    print(i)